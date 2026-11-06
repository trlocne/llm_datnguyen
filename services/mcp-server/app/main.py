# services/mcp-server/app/main.py
# =========================================================
# PURPOSE: Standalone MCP Server microservice — cổng kết nối bên thứ 3.
#          Expose JSON-RPC 2.0 endpoint tại POST /mcp
#          Chat-service gọi vào đây qua MCPHttpClient.
#
# WHAT TO IMPLEMENT:
#   app = FastAPI(title="Enterprise MCP Gateway Server")
#
#   POST /mcp
#     - Parse body là MCPCallToolRequest (JSON-RPC 2.0)
#     - Dispatch theo method:
#         "tools/list"  → router_mcp.list_tools()
#         "tools/call"  → router_mcp.call_tool(name, arguments, user_id)
#     - Return MCPCallToolResponse hoặc MCPListToolsResponse
#
#   GET /auth/{provider}/connect?user_id=...
#     - Redirect user tới OAuth2 authorize URL của provider
#     - Providers: "google_drive", "notion", "confluence", "slack"
#
#   GET /auth/{provider}/callback?code=...&state=user_id
#     - Exchange authorization code → access_token + refresh_token
#     - Lưu token vào Vault tại secret/users/{user_id}/{provider}
#     - Redirect về frontend success page
#
#   GET /auth/connections?user_id=...
#     - Trả về danh sách providers user đã kết nối
#     - [{provider, connected_at, scopes, account_email}]
#
#   DELETE /auth/{provider}/disconnect?user_id=...
#     - Xoá token của user khỏi Vault
#     - Revoke token với provider nếu hỗ trợ
#
#   GET /healthz → {status, connected_tools, active_users}
#
# LIBRARIES: fastapi, uvicorn, httpx (OAuth exchange)
# =========================================================
