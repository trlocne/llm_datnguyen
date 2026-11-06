# services/mcp-server/app/routers/auth_router.py
# =========================================================
# PURPOSE: OAuth2 connect/disconnect/status endpoints cho mỗi provider.
#          User vào trang Admin → bấm "Connect Google Drive" → redirect qua đây.
#
# WHAT TO IMPLEMENT:
#   router = APIRouter(prefix="/auth")
#
#   GET /{provider}/connect
#     Query params: user_id (required)
#     - Validate provider nằm trong PROVIDER_CONFIGS
#     - Gọi oauth_manager.get_authorize_url(provider, user_id)
#     - Return RedirectResponse(url=authorize_url, status_code=302)
#
#   GET /{provider}/callback
#     Query params: code, state (state = user_id truyền từ bước trước)
#     - Gọi await oauth_manager.exchange_code_for_token(provider, code, user_id=state)
#     - Lưu token qua token_store.save_token(...)
#     - Redirect về: {FRONTEND_URL}/admin/connections?connected={provider}&user_id={state}
#     - Nếu lỗi (code không hợp lệ): redirect về /admin/connections?error=...
#
#   GET /connections
#     Query params: user_id
#     - Gọi await token_store.get_connection_metadata(user_id)
#     - Return [{provider, account_email, connected_at, scopes, status}]
#
#   DELETE /{provider}/disconnect
#     Query params: user_id
#     - Gọi await oauth_manager.revoke_token(provider, user_id)
#     - Return {status: "disconnected", provider}
#
# LIBRARIES: fastapi (RedirectResponse, APIRouter), app/auth/oauth_manager.py
# =========================================================
