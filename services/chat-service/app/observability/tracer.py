# observability/tracer.py
# =========================================================
# PURPOSE: Setup tập trung cho OpenTelemetry (Tempo) + Langfuse client.
#
# WHAT TO IMPLEMENT:
#   Function: setup_telemetry() → Tracer
#     - Tạo TracerProvider với Resource(service.name=settings.SERVICE_NAME)
#     - Tạo OTLPSpanExporter(endpoint=settings.OTLP_ENDPOINT, insecure=True)
#     - Attach BatchSpanProcessor vào provider
#     - Gọi trace.set_tracer_provider(provider)
#     - Return trace.get_tracer(settings.SERVICE_NAME)
#
#   Function: get_langfuse_client() → Langfuse
#     - Khởi tạo Langfuse(public_key=..., secret_key=..., host=...) từ settings
#     - Return client singleton
#
#   Export: tracer (OpenTelemetry), langfuse_client (Langfuse)
#     → Các module khác import từ đây
#
# LIBRARIES: opentelemetry-api, opentelemetry-sdk,
#            opentelemetry-exporter-otlp-proto-grpc, langfuse
# =========================================================
