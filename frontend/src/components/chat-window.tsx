# frontend/src/components/chat-window.tsx
# =========================================================
# PURPOSE: Component render danh sách messages với Markdown và streaming cursor.
#
# WHAT TO IMPLEMENT:
#   Props: { messages: ChatMessage[], isStreaming: boolean }
#
#   Render mỗi ChatMessage:
#     - role="user"      → bubble bên phải, nền tối hơn
#     - role="assistant" → bubble bên trái, có markdown rendering
#       Dùng react-markdown + remark-gfm để render tables, bold, code blocks
#     - Nếu isStreaming và message là last assistant → hiển thị blinking cursor
#
#   Auto-scroll:
#     - useRef gắn vào bottom div
#     - useEffect: scroll vào cuối mỗi khi messages thay đổi
#
# LIBRARIES: React, react-markdown, remark-gfm, lucide-react
# =========================================================
