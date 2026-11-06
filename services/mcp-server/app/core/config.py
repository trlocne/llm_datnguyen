# services/mcp-server/app/core/config.py
# =========================================================
# PURPOSE: Config loader cho MCP Server — đọc secrets từ Vault.
#
# WHAT TO IMPLEMENT:
#   Class: MCPServerSettings
#     reload_from_vault():
#       - Vault path: secret/data/mcp-server
#       - Required secrets:
#           GOOGLE_CLIENT_ID       (OAuth2 App credentials)
#           GOOGLE_CLIENT_SECRET
#           GOOGLE_REDIRECT_URI    (vd: http://localhost:8003/auth/google_drive/callback)
#           NOTION_CLIENT_ID
#           NOTION_CLIENT_SECRET
#           NOTION_REDIRECT_URI
#           SLACK_CLIENT_ID
#           SLACK_CLIENT_SECRET
#           VAULT_ADDR             (để lưu per-user tokens)
#           VAULT_TOKEN
#           DATABASE_URL           (lưu metadata kết nối)
#
# settings = MCPServerSettings()  (singleton)
#
# LIBRARIES: hvac, os, logging
# =========================================================
