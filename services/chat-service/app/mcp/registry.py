# mcp/registry.py
# =========================================================
# PURPOSE: Central registry quản lý tất cả Skills (local) và MCP Servers (remote).
#          Là cầu nối giữa Agent và các tool implementations.
#
# WHAT TO IMPLEMENT:
#   Class: MCPRegistry
#     __init__()
#       - self._skills: Dict[str, AbstractSkill]      (tool name → local skill)
#       - self._mcp_clients: Dict[str, AbstractMCPClient] (server name → http client)
#
#     def register_skill(skill: AbstractSkill)
#       - Thêm skill vào self._skills[skill.name]
#
#     def register_mcp_server(server_name, client: AbstractMCPClient)
#       - Thêm client vào self._mcp_clients[server_name]
#
#     async get_all_tool_schemas() → List[dict]
#       - Lấy schema từ tất cả local skills (gọi skill.to_openai_tool_schema())
#       - Lấy schema từ tất cả MCP servers (gọi await client.list_tools())
#       - Merge và return danh sách tools format OpenAI Function Calling
#
#     async execute_tool(tool_name, arguments) → SkillResult
#       - Check self._skills trước → nếu có, gọi skill.execute(**arguments)
#       - Nếu không → loop qua MCP clients, gọi client.call_tool(name, arguments)
#       - Nếu không tìm thấy → SkillResult(success=False, error="Tool not found")
#
#   Export: mcp_registry = MCPRegistry()   (global singleton)
#     → Đăng ký default skills tại đây:
#         mcp_registry.register_skill(SQLDatabaseSkill())
#         mcp_registry.register_skill(GoogleDriveSkill())
#
# LIBRARIES: skills/base.py, mcp/client.py, typing
# =========================================================
