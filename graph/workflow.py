"""Workflow graph wiring for the agent.

This module composes the functional nodes defined in graph.nodes into a
LangGraph StateGraph and provides a helper to execute the pipeline once.
"""

from typing import Any, Dict, List, Optional

import uuid
from langgraph.graph import END, StateGraph

from graph.nodes import (
    AgentState,
    ensure_state_defaults,
    perception_node,
    goal_setting_node,
    memory_recall_node,
    reasoning_node,
    planning_node,
    action_node,
    feedback_node,
    memory_write_node,
)


def is_task_complete(state: AgentState) -> bool:
    """Determine if the current workflow task is complete.

    Heuristic:
    - If there is no plan, consider the task complete.
    - If the number of action_results equals the number of plan steps and all
      are "ok", consider the task complete.

    Args:
        state: Agent workflow state.

    Returns:
        True if the task is complete, False otherwise.
    """
    plan: List[str] = state.get("plan", [])
    results: List[str] = state.get("action_results", [])

    if not plan:
        return True

    if plan and len(results) >= len(plan) and all(r == "ok" for r in results[: len(plan)]):
        return True

    return False


# Build the graph
graph = StateGraph(AgentState)

# Nodes
graph.add_node("Perception", perception_node)
graph.add_node("GoalSetting", goal_setting_node)
graph.add_node("MemoryRecall", memory_recall_node)
graph.add_node("Reasoning", reasoning_node)
graph.add_node("Planning", planning_node)
graph.add_node("ToolExecution", action_node)
graph.add_node("FeedbackProcessing", feedback_node)
graph.add_node("MemoryWrite", memory_write_node)

# Entry and edges
graph.set_entry_point("Perception")

# Perception -> GoalSetting -> MemoryRecall -> Reasoning -> Planning -> ToolExecution -> Feedback -> MemoryWrite
graph.add_edge("Perception", "GoalSetting")
graph.add_edge("GoalSetting", "MemoryRecall")
graph.add_edge("MemoryRecall", "Reasoning")
graph.add_edge("Reasoning", "Planning")
graph.add_edge("Planning", "ToolExecution")
graph.add_edge("ToolExecution", "FeedbackProcessing")
graph.add_edge("FeedbackProcessing", "MemoryWrite")


def should_continue(state: AgentState) -> str:
    """Router to control loop after memory write."""
    return "continue" if not is_task_complete(state) else "end"


graph.add_conditional_edges(
    "MemoryWrite",
    should_continue,
    {
        "continue": "Reasoning",
        "end": END,
    },
)

agent = graph.compile()


def run_graph_once(user_id: Optional[str], session_id: Optional[str], user_input: str) -> AgentState:
    """Execute the node pipeline once in a linear fashion (no graph runtime).

    This helper mirrors the graph ordering and is useful for unit tests and
    simple synchronous executions.

    Args:
        user_id: Optional user identifier; auto-generated if None.
        session_id: Optional session identifier; auto-generated if None.
        user_input: Raw user message.

    Returns:
        The final AgentState produced by the pipeline.
    """
    # Start with minimal inputs and fill defaults to conform to AgentState.
    base_state: Dict[str, Any] = {
        "user_input": user_input,
    }
    state: AgentState = ensure_state_defaults(base_state)

    # Attach non-typed extra metadata commonly used by nodes.
    state["user_id"] = user_id or str(uuid.uuid4())  # type: ignore[index]
    state["session_id"] = session_id or str(uuid.uuid4())  # type: ignore[index]

    # Follow the same order as the graph edges above.
    for fn in [
        perception_node,
        goal_setting_node,
        memory_recall_node,
        reasoning_node,
        planning_node,
        action_node,
        feedback_node,
        memory_write_node,
    ]:
        state = fn(state)

    return state