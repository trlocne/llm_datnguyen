# security/vault/scripts/init-vault.sh
# =========================================================
# PURPOSE: Shell script tự động khởi tạo Vault và nạp secrets khi docker compose up.
#
# WHAT TO IMPLEMENT:
#   1. Wait loop: curl /v1/sys/health cho đến khi Vault online
#   2. Dùng curl + header X-Vault-Token để gọi Vault API:
#      a. Enable KV v2 engine tại mount path "secret/"
#         POST /v1/sys/mounts/secret
#         body: {"type":"kv","options":{"version":"2"}}
#      b. Tạo ACL policy "customer-app-policy":
#         Cho phép read tại: secret/data/customer-chatbot
#         PUT /v1/sys/policies/acl/customer-app-policy
#      c. Write secrets vào secret/data/customer-chatbot:
#         POST /v1/secret/data/customer-chatbot
#         body: {"data": {OPENAI_API_KEY, OPENAI_BASE_URL, DEFAULT_MODEL_NAME,
#                         DATABASE_URL, REDIS_URL,
#                         LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY, LANGFUSE_HOST}}
#         → Các giá trị đọc từ shell $ENV_VAR
#   3. Verify: GET /v1/secret/data/customer-chatbot → check response có key đúng
#   4. Echo status cuối cùng
#
# ENV VARS cần có: VAULT_ADDR, VAULT_DEV_ROOT_TOKEN_ID,
#                  OPENAI_API_KEY, LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY
# =========================================================
