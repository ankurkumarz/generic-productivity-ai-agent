from typing import Dict, Any
def perception_node(state: Dict[str,Any]) -> Dict[str,Any]:
    state['sanitized_input'] = state.get('user_input','').strip()
    state['intent'] = 'general'
    if 'meeting' in state['sanitized_input']:
        state['intent'] = 'schedule_meeting'
    return state
def memory_recall_node(state):
    state['retrieved_memories'] = []
    return state
def reasoning_node(state):
    state['llm_response'] = 'Stub response: planned action'
    return state
def planning_node(state):
    state['plan'] = []
    if state.get('intent')=='schedule_meeting':
        state['plan'].append({'tool':'calendar.create_event','args':{}})
    return state
def action_node(state):
    state['action_results'] = [{'status':'ok'}]
    return state
def feedback_node(state):
    state['explicit_feedback'] = {'rating':5}
    return state
def memory_write_node(state):
    return state
