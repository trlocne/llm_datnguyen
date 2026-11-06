# frontend/src/app/admin/page.tsx
# =========================================================
# PURPOSE: Admin Console - quản lý LLM config, Prompt CMS link, và system info.
#
# WHAT TO IMPLEMENT:
#   "use client" component
#
#   Sections:
#   1. LLM Provider Configuration Panel
#      - Dropdown chọn model (gọi fetchAvailableModels() lúc mount)
#      - Text input cho custom base_url
#      - Slider temperature (0.0 → 1.0)
#      - Button "Apply" → persist settings vào localStorage hoặc gọi backend
#
#   2. Langfuse Prompt CMS Section
#      - Display current active prompt name + version từ Langfuse
#      - Button "Open Langfuse Dashboard" → link http://localhost:3001
#
#   3. Observability Links Panel
#      - Card: "Grafana Dashboard" → http://localhost:3002
#      - Card: "HashiCorp Vault UI" → http://localhost:8200
#      - Card: "Chat API Swagger"  → http://localhost:8001/docs
#
#   4. System Status Panel
#      - Hiển thị health status từ GET /healthz của chat-service và customer-service
#      - Green/Red indicator mỗi service
#
# LIBRARIES: React, next/link, lucide-react (icons)
# =========================================================
