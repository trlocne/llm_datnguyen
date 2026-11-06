# mcp/client.py
# =========================================================
# PURPOSE: MCP Client để chat-service giao tiếp với external MCP Servers qua HTTP/JSON-RPC.
#
# WHAT TO IMPLEMENT:
#   Abstract Class: AbstractMCPClient(ABC)
#     async list_tools()          → List[MCPTool]   (method: tools/list)
#     async call_tool(name, args) → dict             (method: tools/call)
#
#   Class: MCPHttpClient(AbstractMCPClient)
#     __init__(server_url, server_name, timeout_sec)
#
#     async list_tools():
#       - Gửi POST {jsonrpc:"2.0", id:uuid, method:"tools/list", params:{}}
#         tới {server_url}/mcp
#       - Parse response.result["tools"] → List[MCPTool]
#       - Nếu kết nối thất bại → log warning, return []
#
#     async call_tool(tool_name, arguments):
#       - Gửi POST {jsonrpc:"2.0", id:uuid, method:"tools/call",
#                   params:{name:tool_name, arguments:arguments}}
#       - Nếu response có "error" → raise RuntimeError
#       - Return response["result"]
#
# MCP SERVERS CÓ THỂ CONNECT:
#   - google-drive-mcp  (tự build hoặc dùng: https://github.com/modelcontextprotocol/servers)
#   - postgres-mcp      (community MCP server cho PostgreSQL)
#   - Custom MCP server tự viết (FastAPI + JSON-RPC endpoint /mcp)
#
# LIBRARIES: httpx (async), abc, uuid, mcp/protocol.py
# =========================================================
