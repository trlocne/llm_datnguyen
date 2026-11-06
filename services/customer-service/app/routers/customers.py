# services/customer-service/app/routers/customers.py
# =========================================================
# PURPOSE: REST API endpoints cho Customer 360 analytics.
#
# WHAT TO IMPLEMENT:
#   router = APIRouter(prefix="/api/v1/customers")
#
#   Helper: def mask_pii(text) → str
#     - Ẩn phần giữa của customer_id/email cho GDPR compliance
#       Ví dụ: "abc123def456" → "abc****456"
#
#   GET /{customer_id}/360
#     - Query JOIN: customers + orders + order_payments + order_reviews
#     - Return: {customer_id_masked, customer_city, customer_state,
#                total_orders, lifetime_spent, avg_review_score, latest_purchase}
#     - Raise 404 nếu customer_id không tồn tại
#
#   GET /top-spenders?state=SP&limit=10
#     - GROUP BY customer, SUM(payment_value) DESC
#     - Filter theo state nếu có (UPPER compare)
#     - Trả list [{customer_id, city, state, total_orders, total_spent}]
#
#   GET /rfm-analysis
#     - Tính RFM segments:
#         VIP / High Value  → total_spent > 1000
#         Mid-Tier          → 300 ≤ total_spent ≤ 1000
#         Standard          → total_spent < 300
#     - Return [{segment, customer_count, avg_spent}]
#
# DB NOTE: Tất cả queries dùng psycopg2 RealDictCursor hoặc SQLAlchemy async session
# LIBRARIES: fastapi, psycopg2-binary (hoặc sqlalchemy + asyncpg)
# =========================================================
