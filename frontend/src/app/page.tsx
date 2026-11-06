# frontend/src/app/page.tsx
# =========================================================
# PURPOSE: Main chatbot page - giao diện hội thoại chính.
#
# WHAT TO IMPLEMENT:
#   "use client" component
#
#   State:
#     messages: ChatMessage[]       (lịch sử hội thoại)
#     input: string                 (ô input text)
#     isStreaming: boolean          (đang nhận token từ SSE)
#     currentModel: string          (model đang chọn)
#     baseUrl: string               (base_url hiện tại)
#     temperature: number           (0.0 - 1.0)
#     activeMetadata: ToolCallMetadata | null  (tool call details cho ToolInspector)
#
#   Handler: handleSend()
#     - Append user message vào messages
#     - Gọi streamChatMessage() từ lib/api.ts
#     - Loop qua SSE events:
#         "token"    → accumulate vào assistant message (live update)
#         "metadata" → set activeMetadata (hiện ToolInspector)
#         "done"     → set isStreaming=false, lưu trace_id
#     - Hiển thị loading indicator khi isStreaming=true
#
#   UI Layout:
#     - Header: logo + link tới Admin page (/admin)
#     - ModelSelector component (trên cùng hoặc sidebar)
#     - Danh sách messages (scroll xuống cuối tự động)
#     - Mỗi assistant message có ToolInspector phía dưới (nếu có metadata)
#     - Thumbs up/down buttons → gọi submitFeedback()
#     - Input box + Send button ở footer
#
# LIBRARIES: React (useState, useRef, useEffect), next/link
#            components: ModelSelector, ToolInspector
# =========================================================
