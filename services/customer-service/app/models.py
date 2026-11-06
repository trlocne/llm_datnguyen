# services/customer-service/app/models.py
# =========================================================
# PURPOSE: SQLAlchemy ORM models mapping sang Olist PostgreSQL schema.
#
# WHAT TO IMPLEMENT:
#   Base = declarative_base()
#
#   class Customer(Base)
#     __tablename__ = "customers"
#     Columns: customer_id (PK), customer_unique_id, customer_zip_code_prefix,
#              customer_city, customer_state
#     Relationship: orders → List[Order]
#
#   class Order(Base)
#     __tablename__ = "orders"
#     Columns: order_id (PK), customer_id (FK), order_status,
#              order_purchase_timestamp, order_delivered_customer_date,
#              order_estimated_delivery_date
#     Relationship: customer, items, payments, reviews
#
#   class OrderItem(Base)
#     __tablename__ = "order_items"
#     Columns: order_id (FK, PK), order_item_id (PK), product_id,
#              seller_id, price (Numeric), freight_value (Numeric)
#
#   class OrderPayment(Base)
#     __tablename__ = "order_payments"
#     Columns: order_id (FK, PK), payment_sequential (PK),
#              payment_type, payment_installments, payment_value (Numeric)
#
#   class OrderReview(Base)
#     __tablename__ = "order_reviews"
#     Columns: review_id (PK), order_id (FK), review_score (Int),
#              review_comment_title (Text), review_comment_message (Text),
#              review_creation_date (DateTime)
#
# LIBRARIES: sqlalchemy (declarative_base, Column, relationship, etc.)
# =========================================================
