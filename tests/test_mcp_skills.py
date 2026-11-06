# tests/test_mcp_skills.py
# =========================================================
# PURPOSE: Unit tests cho Milestone 3 - MCP & Custom Skills.
#          Sinh viên chạy: pytest tests/test_mcp_skills.py -v
#
# WHAT TO TEST:
#   - test_google_drive_skill_schema:
#       Verify to_openai_tool_schema() output đúng format:
#       {"type":"function", "function": {"name": "google_drive_document_search", ...}}
#       "query" phải nằm trong required fields
#
#   - test_google_drive_skill_mock_execution:
#       await drive_skill.execute(query="SLA contract") → SkillResult
#       result.success == True
#       len(result.data) > 0
#       result.data[0] phải có: "file_id", "file_name", "snippet", "link"
#
#   - test_mcp_registry_unification:
#       Khởi tạo MCPRegistry
#       register_skill(SQLDatabaseSkill())
#       register_skill(GoogleDriveSkill())
#       schemas = await registry.get_all_tool_schemas()
#       Verify 2 schemas với đúng names:
#         "olist_sql_database_query" và "google_drive_document_search"
#
# LIBRARIES: pytest, pytest-asyncio, app.skills.*, app.mcp.registry
# =========================================================
