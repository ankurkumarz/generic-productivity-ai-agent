from fastapi import APIRouter
from pydantic import BaseModel
from main import agent_run_once, mcp_adapter
router = APIRouter()
class InteractReq(BaseModel):
    user_id: str | None = None
    session_id: str | None = None
    input: str
class FeedbackReq(BaseModel):
    session_id: str
    rating: int
    correction: str | None = None
@router.post('/interact')
async def interact(req: InteractReq):
    out = agent_run_once(req.user_id, req.session_id, req.input)
    return out
@router.post('/feedback')
async def feedback(req: FeedbackReq):
    return {'status':'ok'}
@router.get('/tools/discover')
async def discover_tools():
    return mcp_adapter.list_tools()
