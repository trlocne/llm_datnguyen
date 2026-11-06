# services/mcp-server/app/routers/mcp_router.py
# =========================================================
# PURPOSE: JSON-RPC 2.0 endpoint — xử lý tools/list và tools/call.
#          Đây là endpoint chat-service MCPHttpClient gọi tới.
#
# WHAT TO IMPLEMENT:
#   router = APIRouter()
#
#   ALL_TOOLS dict (catalog toàn bộ tools có thể dùng):
#     "google_drive_search":    metadata + required_provider="google_drive"
#     "google_drive_read_file": metadata + required_provider="google_drive"
#     "notion_search_pages":    metadata + required_provider="notion"
#     "notion_read_page":       metadata + required_provider="notion"
#     "slack_list_channels":    metadata + required_provider="slack"
#     "slack_read_messages":    metadata + required_provider="slack"
#
#   POST /mcp
#     Body: {jsonrpc, id, method, params}
#     Header: X-User-ID: <user_id>  ← chat-service phải truyền user_id
#
#     if method == "tools/list":
#       - Lấy user_id từ header
#       - Gọi token_store.list_connected_providers(user_id)
#       - Chỉ trả về tools mà provider đã được connect bởi user đó
#       - Nếu user chưa connect provider nào → trả empty list + hint message
#
#     if method == "tools/call":
#       - Parse params.name + params.arguments + user_id
#       - Lookup tool → biết required_provider
#       - Load token: await token_store.load_token(user_id, required_provider)
#       - Nếu token None → return error "Provider not connected. Please connect at /auth/..."
#       - Dispatch tới tool handler tương ứng (connector module)
#       - Return MCPCallToolResponse với result
#
# LIBRARIES: fastapi, app/auth/token_store.py, app/connectors/*.py
# =========================================================
