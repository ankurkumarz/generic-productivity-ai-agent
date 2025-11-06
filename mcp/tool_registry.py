class ToolRegistry:
    def __init__(self):
        self._tools = {}
    def register(self, name, meta, func):
        self._tools[name] = {'meta':meta,'func':func}
    def get_tools_metadata(self):
        return {k:v['meta'] for k,v in self._tools.items()}
    def get_tool(self, name):
        return self._tools.get(name,{}).get('func')
registry = ToolRegistry()
