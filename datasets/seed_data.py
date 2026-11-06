# datasets/seed_data.py
# =========================================================
# PURPOSE: ETL pipeline nạp dữ liệu Olist CSV vào PostgreSQL + tạo pgvector embeddings.
#
# WHAT TO IMPLEMENT:
#   Constants: DB connection params đọc từ os.environ
#
#   DDL_SCHEMA (SQL string)
#     - CREATE EXTENSION IF NOT EXISTS vector
#     - DROP + CREATE các bảng: customers, products, orders, order_items,
#       order_payments, order_reviews
#     - CREATE TABLE order_review_embeddings (embedding vector(1536))
#     - CREATE INDEX HNSW: USING hnsw (embedding vector_cosine_ops)
#
#   def generate_mock_vector(dim=1536) → List[float]
#     - Sinh random vector dim chiều, chuẩn hóa thành unit vector
#
#   def ingest_from_csv(cur, data_dir)
#     - Đọc từng file CSV trong data_dir bằng pandas
#     - Dùng psycopg2 execute_batch() để bulk insert
#     - Xử lý datetime parsing cho các timestamp columns
#     - Tạo embeddings cho order_reviews (gọi OpenAI API hoặc mock vector)
#
#   def generate_synthetic_data(cur)
#     - Nếu không có CSV → tạo >= 500 customers, >= 100 products, >= 1000 orders
#       với Faker hoặc random + cities/states thực của Brazil
#     - Tạo order_reviews tương ứng + order_review_embeddings với mock vectors
#
#   def main()
#     - Connect psycopg2 → chạy DDL_SCHEMA
#     - Check if data_dir/olist_customers_dataset.csv tồn tại:
#         YES → ingest_from_csv()
#         NO  → generate_synthetic_data()
#     - Commit, verify counts, close connection
#
# LIBRARIES: psycopg2-binary, pandas, faker, tqdm
# RUN: python3 datasets/seed_data.py (sau khi docker compose up -d postgres)
# =========================================================
