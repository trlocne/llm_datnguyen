# tests/test_vault_client.py
# =========================================================
# PURPOSE: Unit tests cho Milestone 4 - HashiCorp Vault integration.
#          Sinh viên chạy: pytest tests/test_vault_client.py -v
#
# WHAT TO TEST:
#   - test_vault_fallback_mechanism:
#       Khởi tạo VaultSecretManager với vault_url trỏ port giả (không tồn tại)
#       max_retries=1, retry_delay_sec=0.1 (nhanh)
#       Gọi fetch_secrets() → phải fallback về os.environ
#       Verify: secrets["OPENAI_BASE_URL"] == os.environ["OPENAI_BASE_URL"]
#       Verify: manager.get_secret("DEFAULT_MODEL_NAME") trả về giá trị đúng
#
#   (Nếu có Vault running) test_vault_real_connection:
#       Khởi tạo với vault_url="http://localhost:8200", token="super-secret-vault-token"
#       fetch_secrets() trả về dict có key "OPENAI_BASE_URL"
#       Không có exception
#
# LIBRARIES: pytest, security.vault.vault_client (VaultSecretManager)
# =========================================================
