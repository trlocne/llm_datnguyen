# routers/chat.py
# =========================================================
# PURPOSE: SSE Streaming endpoint + Feedback endpoint cho chat-service.
#
# WHAT TO IMPLEMENT:
#   Model: ChatRequest (Pydantic BaseModel)
#     Fields: message, model_name, base_url, api_key, temperature, conversation_id
#
#   Model: FeedbackRequest
#     Fields: trace_id, score (1.0 = thumbs up / 0.0 = thumbs down), comment
#
#   GET /models
#     - Trả về current_default_model, current_base_url, danh sách recommended_models
#       (kéo từ settings, không hardcode)
#
#   POST /stream  → EventSourceResponse (SSE)
#     Luồng xử lý:
#       1. Tạo Langfuse trace mới (langfuse_client.trace())
#       2. Khởi tạo CustomerIntelligenceAgent với model/base_url/api_key của request
#       3. Gọi agent.run_turn(message, history)
#       4. Emit SSE events:
#           - event: "status"   → {"status": "thinking" | "executing_tool"}
#           - event: "metadata" → tool call details (SQL query, Drive results, etc.)
#           - event: "token"    → từng token text streaming
#           - event: "done"     → {trace_id, total_latency_ms}
#       5. Stream token-by-token dùng sse-starlette EventSourceResponse
#       6. Update Langfuse trace với output + metadata khi done
#
#   POST /feedback
#     - Nhận trace_id + score từ FeedbackRequest
#     - Gọi langfuse_client.score(trace_id, name="user_satisfaction", value=score)
#
# LIBRARIES: fastapi, sse-starlette, langfuse, pydantic
# =========================================================
