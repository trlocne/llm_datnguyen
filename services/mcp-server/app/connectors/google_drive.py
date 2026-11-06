# services/mcp-server/app/connectors/google_drive.py
# =========================================================
# PURPOSE: Google Drive connector — thực thi tools sau khi có access_token của user.
#          Mỗi lần call phải dùng token của đúng user đó (per-user isolation).
#
# WHAT TO IMPLEMENT:
#   Class: GoogleDriveConnector
#     __init__(access_token: str)
#       - Build google drive service:
#           credentials = google.oauth2.credentials.Credentials(token=access_token)
#           self.service = build("drive", "v3", credentials=credentials)
#       - Hoặc: dùng httpx với header Authorization: Bearer {access_token}
#         (không cần google SDK, nhẹ hơn)
#
#     async def search_files(query: str, max_results: int = 5) → List[dict]
#       - GET https://www.googleapis.com/drive/v3/files
#         params: q=fullText contains '{query}' and trashed=false
#                 fields=files(id,name,mimeType,webViewLink,modifiedTime,owners)
#                 pageSize=max_results
#         headers: Authorization: Bearer {access_token}
#       - Return list [{file_id, name, mime_type, link, modified_at, owner_email}]
#
#     async def read_file_content(file_id: str, mime_type: str) → str
#       - Nếu mime_type == "application/vnd.google-apps.document":
#           GET /drive/v3/files/{file_id}/export?mimeType=text/plain
#       - Nếu mime_type == "application/pdf":
#           GET /drive/v3/files/{file_id}?alt=media  → binary → dùng pdfplumber
#       - Nếu mime_type == "text/plain":
#           GET /drive/v3/files/{file_id}?alt=media  → decode UTF-8
#       - Truncate output tới 2000 ký tự nếu quá dài
#       - Return plain text string
#
#     async def get_file_metadata(file_id: str) → dict
#       - GET /drive/v3/files/{file_id}?fields=id,name,mimeType,owners,createdTime
#       - Return metadata dict
#
# TOOL DEFINITIONS (export để mcp_router dùng):
#   TOOL_GOOGLE_DRIVE_SEARCH = MCPTool(
#     name="google_drive_search",
#     description="Search files in the user's personal Google Drive. Use for contracts, invoices, PDFs, Docs.",
#     inputSchema=MCPToolInputSchema(
#       properties={"query": {"type":"string", "description":"Search keyword"},
#                   "max_results": {"type":"integer"}},
#       required=["query"]
#     )
#   )
#   TOOL_GOOGLE_DRIVE_READ = MCPTool(name="google_drive_read_file", ...)
#
# LIBRARIES: httpx (async), google-auth, pdfplumber (optional)
# =========================================================
