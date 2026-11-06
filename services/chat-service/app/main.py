# main.py  (chat-service)
# =========================================================
# PURPOSE: FastAPI entrypoint cho chat-service.
#
# WHAT TO IMPLEMENT:
#   - Khởi tạo app = FastAPI(title=..., lifespan=...)
#   - Lifespan event:
#       + startup: gọi settings.reload_from_vault() để load secrets
#       + shutdown: flush Langfuse traces, close DB pool
#   - Add middleware:
#       + CORSMiddleware (allow_origins=["*"])
#   - Mount Prometheus metrics:
#       + Dùng prometheus-fastapi-instrumentator, expose tại /metrics
#   - Register routers:
#       + chat.router (prefix /api/v1)
#   - Health check endpoint GET /healthz → trả {status, service, model}
#   - Configure JSON structured logging (python-json-logger)
#     mỗi log record phải có: trace_id, service, level, message
#
# LIBRARIES: fastapi, uvicorn, prometheus-fastapi-instrumentator,
#            python-json-logger, opentelemetry-instrumentation-fastapi
# =========================================================
