# skills/drive_skill.py
# =========================================================
# PURPOSE: Custom Skill cho phép AI Agent đọc tài liệu từ Google Drive
#          (hợp đồng khách hàng, chính sách hoàn tiền, SLA terms).
#
# WHAT TO IMPLEMENT:
#   Class: GoogleDriveSkill(AbstractSkill)
#     name        = "google_drive_document_search"
#     description = "Search and read customer contracts, SLAs, refund policies on Google Drive"
#     parameters  = [
#       SkillParameter("query",       type="string",  required=True),
#       SkillParameter("max_results", type="integer", required=False)
#     ]
#
#     __init__(service_account_json_path=None)
#       - Nếu có path → gọi _init_drive_service()
#       - Nếu không   → chạy Mock Mode
#
#     def _init_drive_service()
#       - Dùng google-api-python-client + google-auth-httplib2:
#           credentials = service_account.Credentials.from_service_account_file(path, scopes=[...])
#           self._drive_service = build("drive", "v3", credentials=credentials)
#
#     async search_drive_files(query, max_results) → List[dict]
#       - Gọi self._drive_service.files().list(
#             q=f"fullText contains '{query}'",
#             fields="files(id,name,mimeType,webViewLink)",
#             pageSize=max_results
#         ).execute()
#       - Return list[{file_id, name, mime_type, web_view_link}]
#       - MOCK MODE: Return 3 bản ghi fake (SLA, Refund Policy, VIP Terms)
#
#     async extract_file_content(file_id) → str
#       - Google Docs → drive_service.files().export_media(mimeType="text/plain")
#       - PDF         → tải binary rồi dùng pdfplumber/pypdf để extract text
#       - MOCK MODE   → return string cứng tương ứng với file_id
#
#     async execute(**kwargs) → SkillResult
#       - search_drive_files() → loop từng file → extract_file_content()
#       - Build result list: [{file_id, file_name, snippet(800 chars), link}]
#       - Return SkillResult(success, data=list, metadata={total_found})
#
# LIBRARIES: google-api-python-client, google-auth-httplib2,
#            pdfplumber (PDF), skills/base.py
# MCP NOTE: File này cũng có thể được wrap thành MCP Server riêng
#           rồi chat-service gọi qua MCPHttpClient
# =========================================================
