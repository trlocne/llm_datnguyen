# services/mcp-server/app/auth/token_store.py
# =========================================================
# PURPOSE: Per-user token storage trong HashiCorp Vault KV v2.
#          Mỗi user có vault path riêng — cô lập hoàn toàn.
#
# VAULT PATH SCHEME:
#   secret/data/users/{user_id}/google_drive  → {access_token, refresh_token, expires_at, email, scopes}
#   secret/data/users/{user_id}/notion        → {access_token, workspace_id, ...}
#   secret/data/users/{user_id}/slack         → {access_token, team_id, ...}
#
# WHAT TO IMPLEMENT:
#   Class: UserTokenStore
#     __init__(vault_client: hvac.Client)
#
#     def _build_path(user_id, provider) → str
#       - Return "users/{user_id}/{provider}"
#
#     async def save_token(user_id, provider, token_data: dict) → None
#       - Write vào Vault KV v2: mount=secret, path=users/{user_id}/{provider}
#       - token_data chứa: access_token, refresh_token (nếu có),
#         expires_at (timestamp), scope, account_email
#
#     async def load_token(user_id, provider) → dict | None
#       - Read từ Vault path
#       - Nếu không tìm thấy → return None
#       - Check expires_at: nếu gần hết hạn (< 5 phút) → auto-refresh qua oauth_manager
#
#     async def delete_token(user_id, provider) → None
#       - Vault KV v2 delete: client.secrets.kv.v2.delete_latest_version_of_secret(...)
#
#     async def list_connected_providers(user_id) → List[str]
#       - Vault KV v2 list: list tất cả secret paths dưới users/{user_id}/
#       - Return danh sách provider names user đã connect
#
#     async def get_connection_metadata(user_id) → List[dict]
#       - Với mỗi provider đã connect, load metadata: {provider, account_email, connected_at, scopes}
#       - Return list để hiển thị trên UI
#
# LIBRARIES: hvac, datetime
# =========================================================
