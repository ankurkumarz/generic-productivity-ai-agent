import uvicorn
from fastapi import FastAPI
from api import routes
from mcp.mcp_adapter import mcp_adapter
app = FastAPI(title='Agentic Productivity Helper')
app.include_router(routes.router)
try:
    from mcp.mcp_adapter import mcp_server
    app.mount('/mcp', mcp_server.as_fastapi_router())
except Exception:
    pass
@app.get('/health')
async def health():
    return {'status':'ok'}
# expose for routes
from graph.workflow import run_graph_once as agent_run_once  # noqa
if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080, reload=True)
