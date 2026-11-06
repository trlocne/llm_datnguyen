# frontend/src/components/tool-inspector.tsx
# =========================================================
# PURPOSE: Collapsible visual drawer hiển thị thông tin tool execution.
#
# WHAT TO IMPLEMENT:
#   Props: { metadata: ToolCallMetadata | null }
#
#   Nếu metadata là null → return null (không render gì)
#
#   Hiển thị dựa trên metadata.mode:
#     "text_to_sql":
#       - Badge màu xanh lá "SQL Query"
#       - Code block hiển thị metadata.sql (highlight PostgreSQL syntax)
#       - Stats row: execution_ms, row_count, columns (comma-separated)
#
#     "semantic_rag":
#       - Badge màu tím "Vector Search"
#       - Hiển thị số review tìm được, preview snippet
#
#     "mcp_tool" (Drive):
#       - Badge màu cam "Google Drive"
#       - Danh sách file tìm được với link clickable
#
#   Footer chung:
#     - Langfuse Trace ID (link: http://localhost:3001/trace/{trace_id})
#     - Tổng latency ms
#
# LIBRARIES: React, lucide-react (Database, FileText, Clock icons)
# =========================================================
