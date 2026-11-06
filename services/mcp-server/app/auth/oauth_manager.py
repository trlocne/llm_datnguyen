# services/mcp-server/app/auth/oauth_manager.py
# =========================================================
# PURPOSE: Per-user OAuth2 flow manager cho mọi third-party provider.
#          Mỗi user có token riêng lưu trong Vault — KHÔNG share.
#
# WHAT TO IMPLEMENT:
#
#   PROVIDER_CONFIGS dict (định nghĩa sẵn, không hardcode trong routes):
#     "google_drive": {
#       authorize_url: "https://accounts.google.com/o/oauth2/v2/auth",
#       token_url:     "https://oauth2.googleapis.com/token",
#       revoke_url:    "https://oauth2.googleapis.com/revoke",
#       scopes: ["https://www.googleapis.com/auth/drive.readonly",
#                "https://www.googleapis.com/auth/drive.metadata.readonly"],
#       client_id:     settings.GOOGLE_CLIENT_ID,
#       client_secret: settings.GOOGLE_CLIENT_SECRET,
#       redirect_uri:  settings.GOOGLE_REDIRECT_URI,
#     }
#     "notion": { ... }
#     "slack":  { ... }
#     "confluence": { ... }
#
#   def get_authorize_url(provider, user_id) → str
#     - Build OAuth2 URL với state=user_id (để callback biết user nào)
#     - Thêm params: client_id, redirect_uri, scope, response_type=code,
#                    access_type=offline (Google), prompt=consent
#     - Return URL string để redirect user
#
#   async def exchange_code_for_token(provider, code, user_id) → TokenData
#     - POST tới provider token_url với:
#         grant_type=authorization_code, code, redirect_uri, client_id, client_secret
#     - Parse response: {access_token, refresh_token, expires_in, token_type, scope}
#     - Gọi save_user_token(user_id, provider, token_data)
#     - Return TokenData
#
#   async def refresh_access_token(provider, user_id) → str
#     - Load refresh_token từ Vault
#     - POST tới token_url với grant_type=refresh_token
#     - Update access_token trong Vault
#     - Return new access_token
#
#   async def revoke_token(provider, user_id) → bool
#     - GET hoặc POST tới provider revoke_url với token
#     - Gọi delete_user_token(user_id, provider)
#
# LIBRARIES: httpx (async HTTP), urllib.parse
# =========================================================
