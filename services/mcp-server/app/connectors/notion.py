# services/mcp-server/app/connectors/notion.py
# =========================================================
# PURPOSE: Notion connector — search và đọc pages từ workspace của user.
#
# WHAT TO IMPLEMENT:
#   Class: NotionConnector
#     __init__(access_token: str)
#       - base_url = "https://api.notion.com/v1"
#       - headers = {Authorization: Bearer {access_token}, Notion-Version: "2022-06-28"}
#
#     async def search_pages(query: str, max_results: int = 5) → List[dict]
#       - POST /v1/search
#         body: {query: query, filter: {value: "page", property: "object"}, page_size: max_results}
#       - Return [{page_id, title, url, last_edited_time}]
#
#     async def read_page_content(page_id: str) → str
#       - GET /v1/blocks/{page_id}/children  → list of blocks
#       - Flatten block content:
#           paragraph → text
#           heading_1/2/3 → markdown heading
#           bulleted_list_item → "• text"
#           code → fenced code block
#       - Return concatenated string
#
# TOOL DEFINITIONS:
#   TOOL_NOTION_SEARCH = MCPTool(name="notion_search_pages", ...)
#   TOOL_NOTION_READ   = MCPTool(name="notion_read_page", ...)
#
# LIBRARIES: httpx (async)
# =========================================================
