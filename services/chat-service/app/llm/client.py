# llm/client.py
# =========================================================
# PURPOSE: Dynamic LLM client factory tương thích mọi OpenAI-compatible backend.
#
# WHAT TO IMPLEMENT:
#   Function: get_openai_client(api_key, base_url) → AsyncOpenAI
#     - Nhận api_key và base_url override từ caller
#     - Fallback về settings.OPENAI_API_KEY / settings.OPENAI_BASE_URL nếu None
#     - Return openai.AsyncOpenAI(api_key=..., base_url=...)
#     - Hỗ trợ cấu hình:
#         OpenAI   → https://api.openai.com/v1
#         DeepSeek → https://api.deepseek.com/v1
#         Groq     → https://api.groq.com/openai/v1
#         Ollama   → http://localhost:11434/v1  (api_key="ollama")
#         vLLM     → http://vllm-host:8000/v1
#
# LIBRARIES: openai (AsyncOpenAI)
# =========================================================
