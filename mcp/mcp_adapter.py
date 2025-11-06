from mcp.tool_registry import registry
class MCPAdapter:
    def __init__(self, registry):
        self.registry = registry
    def list_tools(self):
        return self.registry.get_tools_metadata()
    async def execute(self, tool_name, payload):
        func = self.registry.get_tool(tool_name)
        if not func:
            raise ValueError('tool not found')
        return func(payload)
mcp_adapter = MCPAdapter(registry)
