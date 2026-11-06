# frontend/src/lib/api.ts
# =========================================================
# PURPOSE: TypeScript API client layer cho Frontend Next.js.
#
# WHAT TO IMPLEMENT:
#   Interfaces/Types:
#     ChatMessage { id, role ("user"|"assistant"), content, metadata? }
#     ToolCallMetadata { mode, sql?, execution_ms?, row_count?, columns?,
#                        trace_id?, tools_called? }
#     ModelOption { id, name, provider }
#
#   Function: fetchAvailableModels() → Promise<{...}>
#     - GET /api/v1/chat/models
#     - Return current_default_model, current_base_url, recommended_models[]
#
#   Function: streamChatMessage(params) → AsyncGenerator<SSEEvent>
#     - Gọi fetch("/api/v1/chat/stream", {method: POST, body: JSON.stringify(params)})
#     - Đọc response.body qua ReadableStream + TextDecoder
#     - Parse từng line "data: {...}" → yield event object
#     - Handle các event types: "status", "metadata", "token", "done"
#
#   Function: submitFeedback(trace_id, score, comment?) → Promise<boolean>
#     - POST /api/v1/chat/feedback
#     - Return true nếu thành công
#
# LIBRARIES: (native fetch API, TypeScript generics)
# =========================================================
