from graph.nodes import perception_node, memory_recall_node, reasoning_node, planning_node, action_node, feedback_node, memory_write_node
import uuid
def run_graph_once(user_id, session_id, user_input):
    state = {'user_id': user_id or str(uuid.uuid4()), 'session_id': session_id or str(uuid.uuid4()), 'user_input': user_input}
    for fn in [perception_node, memory_recall_node, reasoning_node, planning_node, action_node, feedback_node, memory_write_node]:
        state = fn(state)
    return state
