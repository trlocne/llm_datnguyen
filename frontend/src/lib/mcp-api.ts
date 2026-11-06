# frontend/src/lib/mcp-api.ts
# =========================================================
# PURPOSE: TypeScript client để giao tiếp với MCP Server từ Frontend.
#
# WHAT TO IMPLEMENT:
#   const MCP_SERVER_URL = process.env.NEXT_PUBLIC_MCP_SERVER_URL || "http://localhost:8003"
#
#   Type: ConnectionStatus
#     { provider, account_email, connected_at, scopes, is_active }
#
#   Function: fetchUserConnections(userId: string) → Promise<ConnectionStatus[]>
#     - GET {MCP_SERVER_URL}/auth/connections?user_id={userId}
#     - Return array của ConnectionStatus
#
#   Function: disconnectProvider(userId: string, provider: string) → Promise<boolean>
#     - DELETE {MCP_SERVER_URL}/auth/{provider}/disconnect?user_id={userId}
#     - Return true nếu success
#
#   Function: getConnectUrl(userId: string, provider: string) → string
#     - Return {MCP_SERVER_URL}/auth/{provider}/connect?user_id={userId}
#     - Dùng để build href của "Connect" button
#
#   Function: callMCPTool(toolName, arguments, userId) → Promise<any>
#     - POST {MCP_SERVER_URL}/mcp
#       headers: X-User-ID: userId, Content-Type: application/json
#       body: {jsonrpc:"2.0", id:uuid, method:"tools/call", params:{name:toolName, arguments}}
#     - Return result hoặc throw error
#
# LIBRARIES: (native fetch, UUID từ crypto.randomUUID())
# =========================================================
