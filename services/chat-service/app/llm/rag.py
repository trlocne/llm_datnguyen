# llm/rag.py
# =========================================================
# PURPOSE: Semantic vector search trên customer reviews dùng pgvector.
#
# WHAT TO IMPLEMENT:
#   async get_embedding(text, api_key, base_url) → List[float]
#     - Gọi openai.embeddings.create(model="text-embedding-3-small", input=text)
#     - Return vector 1536 chiều
#     - Fallback: nếu OpenAI unreachable → sinh random unit vector (dev mode)
#
#   def search_semantic_reviews(query_embedding, limit=5) → List[dict]
#     - Connect PostgreSQL (settings.DATABASE_URL)
#     - Thực thi câu query pgvector:
#         SELECT review_id, review_score, review_text,
#                1 - (embedding <=> %s::vector) AS similarity
#         FROM order_review_embeddings
#         ORDER BY embedding <=> %s::vector ASC
#         LIMIT %s;
#     - Return list[dict] với các field trên
#
# LIBRARIES: openai, psycopg2-binary, pgvector
# NOTE: Bảng order_review_embeddings phải có HNSW index (xem seed_data.py)
# =========================================================
