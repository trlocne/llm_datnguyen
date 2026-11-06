# mcp/protocol.py
# =========================================================
# PURPOSE: Pydantic schemas cho Model Context Protocol (MCP) - JSON-RPC 2.0.
#
# WHAT TO IMPLEMENT (Pydantic BaseModel classes):
#   MCPToolInputSchema
#     Fields: type="object", properties: dict, required: list[str]
#
#   MCPTool
#     Fields: name (str), description (str), inputSchema (MCPToolInputSchema)
#
#   MCPContent
#     Fields: type ("text" | "image" | "data"), text (optional), data (optional)
#
#   MCPCallToolRequest   (JSON-RPC outgoing)
#     Fields: jsonrpc="2.0", id, method="tools/call",
#             params: {"name": str, "arguments": dict}
#
#   MCPCallToolResponse  (JSON-RPC incoming)
#     Fields: jsonrpc, id, result (optional dict), error (optional dict)
#
#   MCPListToolsResponse (JSON-RPC incoming)
#     Fields: jsonrpc, id, result: {"tools": List[MCPTool]}
#
# NOTE: Các schema này conform với spec tại https://modelcontextprotocol.io
# LIBRARIES: pydantic, typing
# =========================================================
