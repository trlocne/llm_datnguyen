# llm/agent.py
# =========================================================
# PURPOSE: Autonomous ReAct Agent điều phối tool calling giữa SQL và Google Drive.
#
# WHAT TO IMPLEMENT:
#   Class: CustomerIntelligenceAgent
#     __init__(model_name, base_url, api_key)
#       - Khởi tạo LLM client từ llm/client.py
#
#     async run_turn(user_message, conversation_history) → (str, list)
#       - Bước 1: Lấy tất cả tool schemas từ await mcp_registry.get_all_tool_schemas()
#       - Bước 2: Gọi LLM với tools=tool_schemas, tool_choice="auto"
#       - Bước 3: Nếu LLM trả về tool_calls:
#           a. Parse tool name + JSON arguments
#           b. Gọi await mcp_registry.execute_tool(name, arguments)
#           c. Append tool result vào messages
#           d. Gọi LLM lần 2 để tổng hợp final answer
#       - Bước 4: Return (final_text_markdown, executed_tools_list)
#
#   SYSTEM PROMPT phải hướng dẫn model:
#     - Khi nào dùng tool "olist_sql_database_query" (số liệu, stats, ranking)
#     - Khi nào dùng "google_drive_document_search" (hợp đồng, chính sách, SLA)
#     - Khi nào dùng cả hai (đơn trễ → check SQL rồi check Drive refund policy)
#
#   Phải gắn OpenTelemetry span: "agent_reasoning_step" và "agent_synthesis_step"
#
# LIBRARIES: openai, opentelemetry-api, json
# =========================================================
