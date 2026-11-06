# services/mcp-server/app/db/models.py
# =========================================================
# PURPOSE: SQLAlchemy models lưu metadata kết nối (không lưu token — token trong Vault).
#
# WHAT TO IMPLEMENT:
#   Base = declarative_base()
#
#   class UserConnection(Base)
#     __tablename__ = "user_connections"
#     Columns:
#       id          (UUID, PK)
#       user_id     (String, indexed) ← ID của user trong hệ thống chatbot
#       provider    (String) ← "google_drive", "notion", "slack"
#       account_email (String) ← email của tài khoản đã kết nối
#       scopes      (Text) ← space-separated scopes đã được grant
#       connected_at (DateTime, default=now)
#       last_used_at (DateTime, nullable)
#       is_active    (Boolean, default=True)
#
#     Composite unique: (user_id, provider) ← mỗi user chỉ connect 1 account/provider
#
# INDICES: idx_user_connections_user_id, idx_user_connections_provider
#
# PURPOSE OF TABLE:
#   - Hiển thị UI "Connections" page mà không cần gọi Vault
#   - Track last_used_at để analytics
#   - is_active=False khi user disconnect (token đã revoke)
#
# LIBRARIES: sqlalchemy, uuid
# =========================================================
