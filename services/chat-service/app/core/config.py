# config.py
# =========================================================
# PURPOSE: Central settings loader for chat-service.
#
# WHAT TO IMPLEMENT:
#   - Class `Settings` (hoặc dùng pydantic-settings BaseSettings)
#   - On startup: gọi VaultSecretManager.fetch_secrets() từ security/vault/vault_client.py
#   - Nếu Vault không reach được → fallback đọc os.environ
#   - Expose các attr sau để toàn service dùng:
#       OPENAI_API_KEY, OPENAI_BASE_URL, DEFAULT_MODEL_NAME
#       DATABASE_URL, REDIS_URL
#       LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY, LANGFUSE_HOST
#       OTLP_ENDPOINT (Tempo), SERVICE_NAME
#
# LIBRARIES: pydantic-settings, hvac (gián tiếp qua vault_client), python-dotenv
# =========================================================
