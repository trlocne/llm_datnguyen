# services/customer-service/app/core/config.py
# =========================================================
# PURPOSE: Settings loader cho customer-service (đọc từ Vault, fallback env).
#
# WHAT TO IMPLEMENT:
#   Class: Settings
#     reload_from_vault()
#       - Gọi vault_manager.fetch_secrets() từ security/vault/vault_client.py
#       - Set: DATABASE_URL, SERVICE_NAME = "customer-service"
#
# LIBRARIES: hvac (gián tiếp), os
# =========================================================
