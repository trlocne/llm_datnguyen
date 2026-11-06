# services/mcp-server/app/connectors/slack.py
# =========================================================
# PURPOSE: Slack connector — list channels và đọc messages.
#
# WHAT TO IMPLEMENT:
#   Class: SlackConnector
#     __init__(access_token: str)
#       - base_url = "https://slack.com/api"
#       - headers = {Authorization: Bearer {access_token}}
#
#     async def list_channels(limit: int = 20) → List[dict]
#       - GET /conversations.list?types=public_channel,private_channel&limit={limit}
#       - Return [{channel_id, name, is_private, member_count, topic}]
#
#     async def read_channel_messages(channel_id: str, limit: int = 10) → List[dict]
#       - GET /conversations.history?channel={channel_id}&limit={limit}
#       - Return [{ts, user_id, text, reply_count}]
#       - Optionally: resolve user_id → username qua /users.info
#
# TOOL DEFINITIONS:
#   TOOL_SLACK_CHANNELS  = MCPTool(name="slack_list_channels", ...)
#   TOOL_SLACK_MESSAGES  = MCPTool(name="slack_read_messages", ...)
#
# LIBRARIES: httpx (async)
# =========================================================
