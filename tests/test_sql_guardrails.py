# tests/test_sql_guardrails.py
# =========================================================
# PURPOSE: Unit tests cho Milestone 2 - SQL Guardrails.
#          Sinh viên chạy: pytest tests/test_sql_guardrails.py -v
#
# WHAT TO TEST:
#   - test_valid_select_query: SELECT bình thường → pass, tự động thêm LIMIT 100
#   - test_valid_cte_with_query: WITH...SELECT → pass, limit thêm vào
#   - test_reject_multiple_statements: "SELECT...; DROP..." → SQLGuardrailError
#   - test_reject_drop_keyword: "DROP TABLE..." → SQLGuardrailError
#   - test_reject_destructive_dml: DELETE/UPDATE/INSERT/ALTER/TRUNCATE → lỗi
#   - test_reject_catalog_access: "SELECT FROM information_schema.tables" → lỗi
#   - test_row_limit_clamping:
#       + Không có LIMIT   → thêm LIMIT 100
#       + LIMIT 50000      → clamp về LIMIT 100
#       + LIMIT 10         → giữ nguyên LIMIT 10
#
# LIBRARIES: pytest, app.skills.sql_skill (SQLDatabaseSkill, SQLGuardrailError)
# =========================================================
