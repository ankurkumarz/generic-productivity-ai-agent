from typing import Any, Dict, List, TypedDict

__all__ = [
    "AgentState",
    "ensure_state_defaults",
    "perception_node",
    "goal_setting_node",
    "memory_recall_node",
    "reasoning_node",
    "planning_node",
    "action_node",
    "self_reflection_node",
    "feedback_node",
    "memory_write_node",
]


"""
Node definitions for the agent workflow graph.

Each node is a pure function that:
- Accepts a mutable "state" dictionary (AgentState).
- Mutates the state with new keys relevant to its responsibility.
- Returns the same state for downstream nodes.

Nodes included:
- perception_node: Sanitizes input and infers lightweight signals (e.g., entities).
- goal_setting_node: Extracts and persists explicit goals.
- memory_recall_node: Retrieves relevant memories (stub).
- reasoning_node: Produces a model-driven response (stub).
- planning_node: Produces a lightweight execution plan.
- action_node: Executes tools/APIs based on plan (stub).
- self_reflection_node: Reflects on outcomes (stub).
- feedback_node: Records explicit/implicit feedback (stub).
- memory_write_node: Persists new memories (stub).
"""


class AgentState(TypedDict):
    """Typed workflow state shared across all nodes."""
    user_input: str
    sanitized_input: str
    entities: List[str]
    goals: List[str]
    plan: List[str]
    action_results: List[str]
    memories_retrieved: List[str]
    memories_to_write: List[str]
    feedback: Dict[str, Any]
    response: str


def ensure_state_defaults(state: Dict[str, Any]) -> AgentState:
    """Return AgentState with defaults for any missing keys.

    Args:
        state: A possibly-partial state mapping.

    Returns:
        A fully-populated AgentState with sensible defaults.
    """
    typed: AgentState = {
        "user_input": str(state.get("user_input", "")),
        "sanitized_input": str(state.get("sanitized_input", "")),
        "entities": list(state.get("entities", [])),
        "goals": list(state.get("goals", [])),
        "plan": list(state.get("plan", [])),
        "action_results": list(state.get("action_results", [])),
        "memories_retrieved": list(state.get("memories_retrieved", [])),
        "memories_to_write": list(state.get("memories_to_write", [])),
        "feedback": state.get("feedback"),
        "response": str(state.get("response", "")),
    }
    return typed


def perception_node(state: AgentState) -> AgentState:
    """Sanitize user input and extract lightweight entities.

    Args:
        state: Workflow state. Expected keys:
            - "user_input": Raw user message.

    Returns:
        The updated state with:
            - "sanitized_input": Trimmed user input.
            - "entities": Naive entity list (e.g., capitalized tokens).
    """
    state = ensure_state_defaults(state)
    text = state["user_input"].strip()
    state["sanitized_input"] = text

    # Naive entity heuristic: capitalized tokens (placeholder for NER).
    if text and not state["entities"]:
        tokens = [w.strip(",.!?;:") for w in text.split()]
        state["entities"] = [w for w in tokens if w[:1].isupper()]

    return state


def goal_setting_node(state: AgentState) -> AgentState:
    """Extract explicit goals from sanitized input and append to state.

    Treats a sufficiently long or punctuated sentence as a goal.

    Args:
        state: Workflow state. Expected keys:
            - "sanitized_input": Cleaned user text.
            - "goals": Optional list of existing goals.

    Returns:
        The updated state with:
            - "goals": List of goals including any newly extracted goal.
    """
    state = ensure_state_defaults(state)
    text = state["sanitized_input"]

    if text and (text.endswith((".", "!", "?")) or len(text.split()) > 3):
        state["goals"].append(text)

    return state


def memory_recall_node(state: AgentState) -> AgentState:
    """Retrieve relevant memories for the current user and input context.

    This is a stub that illustrates where vector DB retrieval would occur.

    Args:
        state: Workflow state.

    Returns:
        The updated state with:
            - "memories_retrieved": A list of memory snippets (strings).
    """
    state = ensure_state_defaults(state)

    # TODO: Integrate memory retrieval using mem0.ai or pgvector.
    # Placeholder: keep as empty list or attach mock snippets.
    if not state["memories_retrieved"]:
        state["memories_retrieved"] = []

    return state


def reasoning_node(state: AgentState) -> AgentState:
    """Produce a response from context (placeholder for LLM reasoning).

    Args:
        state: Workflow state.

    Returns:
        The updated state with:
            - "response": A placeholder response string.
    """
    state = ensure_state_defaults(state)
    state["response"] = "Stub response: planned action"
    return state


def planning_node(state: AgentState) -> AgentState:
    """Create a simple execution plan based on the sanitized input.

    Args:
        state: Workflow state. Expected keys:
            - "sanitized_input": Cleaned user text.

    Returns:
        The updated state with:
            - "plan": A list of plan step names as strings.
    """
    state = ensure_state_defaults(state)
    plan: List[str] = []

    if "meeting" in state["sanitized_input"].lower():
        plan.append("calendar.create_event")

    state["plan"] = plan
    return state


def action_node(state: AgentState) -> AgentState:
    """Execute planned actions using available tools/APIs (stub).

    Args:
        state: Workflow state. Expected keys:
            - "plan": List of planned steps.

    Returns:
        The updated state with:
            - "action_results": Execution outcomes per step as strings.
    """
    state = ensure_state_defaults(state)

    if state["plan"]:
        state["action_results"] = ["ok" for _ in state["plan"]]
    else:
        state["action_results"] = ["ok"]

    return state


def self_reflection_node(state: AgentState) -> AgentState:
    """Analyze action outcomes and produce reflections or adjustments (stub).

    Args:
        state: Workflow state. Expected keys:
            - "action_results": Outputs from action_node.

    Returns:
        The updated state with:
            - "feedback": A simple placeholder rating or notes.
    """
    state = ensure_state_defaults(state)
    state["feedback"] = {"rating": 5}
    return state


def feedback_node(state: AgentState) -> AgentState:
    """Record user/system feedback signals for learning loops.

    Args:
        state: Workflow state.

    Returns:
        The updated state with:
            - "feedback": Placeholder explicit feedback if not already present.
    """
    state = ensure_state_defaults(state)
    if not state["feedback"]:
        state["feedback"] = {"rating": 5}
    return state


def memory_write_node(state: AgentState) -> AgentState:
    """Persist new memories based on the current state.

    Args:
        state: Workflow state. Expected keys:
            - "memories_to_write": List of memories to be written.

    Returns:
        The updated state.
    """
    state = ensure_state_defaults(state)

    # TODO: Implement memory writing logic.
    # Placeholder: assume memories are written successfully.
    if state["memories_to_write"]:
        state["memories_to_write"] = []

    return state