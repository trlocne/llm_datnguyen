# skills/sql_skill.py
# =========================================================
# PURPOSE: Skill thực thi analytical SQL queries lên Olist PostgreSQL với guardrails.
#
# WHAT TO IMPLEMENT:
#   Exception: SQLGuardrailError(Exception)
#
#   Class: SQLDatabaseSkill(AbstractSkill)
#     name     = "olist_sql_database_query"
#     description = "Execute read-only SQL on Olist e-commerce DB ..."
#     parameters  = [SkillParameter(name="sql_query", type="string", required=True)]
#
#     def validate_ast(sql) → None
#       - Parse bằng sqlparse
#       - Đảm bảo chỉ có đúng 1 statement
#       - Statement phải là SELECT hoặc WITH...SELECT
#       - Raise SQLGuardrailError nếu vi phạm
#
#     def check_blacklisted_keywords(sql) → None
#       - Dùng regex tìm: DROP, DELETE, UPDATE, INSERT, ALTER, TRUNCATE,
#                         GRANT, REVOKE, EXEC, information_schema, pg_catalog
#       - Raise SQLGuardrailError nếu match
#
#     def enforce_row_limit(sql, max_limit=100) → str
#       - Nếu không có LIMIT → append " LIMIT 100"
#       - Nếu LIMIT > 100   → clamp về 100
#       - Return sanitized SQL string
#
#     def execute_read_only(sql) → Tuple[List[dict], float]
#       - Connect psycopg2 với settings.DATABASE_URL
#       - SET TRANSACTION READ ONLY
#       - SET LOCAL statement_timeout = '5000ms'
#       - Fetch rows dùng RealDictCursor
#       - Return (rows, elapsed_ms)
#
#     async execute(**kwargs) → SkillResult
#       - Gọi lần lượt: validate_ast → check_blacklisted → enforce_row_limit → execute_read_only
#       - Return SkillResult(success, data=rows, metadata={sql, row_count, columns})
#
# LIBRARIES: psycopg2-binary, sqlparse, re
# =========================================================
