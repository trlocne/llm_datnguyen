# frontend/src/app/admin/connections/page.tsx
# =========================================================
# PURPOSE: Trang "My Integrations" cho user kết nối tài khoản bên thứ 3.
#          Giống trang Integrations của Zapier / Notion / Linear.
#
# WHAT TO IMPLEMENT:
#   "use client" component
#
#   State:
#     connections: ConnectionStatus[]   (danh sách providers + trạng thái)
#     userId: string                    (lấy từ session / localStorage)
#
#   Type ConnectionStatus:
#     { provider: string, display_name: string, icon: ReactNode,
#       connected: boolean, account_email?: string, connected_at?: string }
#
#   On mount:
#     - Fetch GET /auth/connections?user_id={userId} từ mcp-server
#     - Set connections state
#
#   UI: Grid of integration cards, mỗi card có:
#     [Icon] [Provider Name]
#     [Description: "Access your Google Drive documents..."]
#     [Status badge: "Connected ✓ user@gmail.com" hoặc "Not connected"]
#     [Button]: nếu chưa connect → "Connect" (link đến /auth/{provider}/connect?user_id=...)
#               nếu đã connect  → "Disconnect" (gọi DELETE /auth/{provider}/disconnect)
#
#   PROVIDERS ĐỂ HIỂN THỊ (hardcode metadata, status từ API):
#     - Google Drive  (icon: Google Drive logo)
#     - Notion        (icon: Notion logo)
#     - Slack         (icon: Slack logo)
#     - Confluence    (icon: Confluence logo) ← bonus
#
#   Flow khi click "Connect Google Drive":
#     → window.location.href = "http://mcp-server:8003/auth/google_drive/connect?user_id={userId}"
#     → User bị redirect tới Google OAuth consent screen
#     → Sau khi approve, Google redirect về /auth/google_drive/callback
#     → mcp-server lưu token vào Vault, redirect về trang này
#     → Hiển thị toast "Google Drive connected!"
#
# LIBRARIES: React, next/link, lucide-react
# =========================================================
