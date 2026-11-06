# services/customer-service/app/main.py
# =========================================================
# PURPOSE: FastAPI entrypoint cho customer-service.
#
# WHAT TO IMPLEMENT:
#   - app = FastAPI(title="Customer 360 & Analytics Service")
#   - CORSMiddleware (allow_origins=["*"])
#   - Prometheus metrics: Instrumentator().instrument(app).expose(app, endpoint="/metrics")
#   - Include router: customers.router
#   - GET /healthz → {status, service, database_connected}
#   - Structured JSON logging (python-json-logger)
#
# LIBRARIES: fastapi, uvicorn, prometheus-fastapi-instrumentator
# =========================================================
