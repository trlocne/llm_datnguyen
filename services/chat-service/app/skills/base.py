# skills/base.py
# =========================================================
# PURPOSE: Abstract base class + Pydantic schemas cho toàn bộ Skills/MCP Tools.
#
# WHAT TO IMPLEMENT:
#   Model: SkillParameter (Pydantic BaseModel)
#     Fields: name, type (json schema type), description, required, enum (optional)
#
#   Model: SkillResult (Pydantic BaseModel)
#     Fields: success (bool), data (Any), error_message (Optional[str]),
#             execution_time_ms (float), metadata (dict)
#
#   Abstract Class: AbstractSkill (ABC)
#     Abstract properties:
#       @property name → str           (unique tool identifier)
#       @property description → str    (giải thích cho LLM khi nào dùng tool này)
#       @property parameters → List[SkillParameter]
#
#     Concrete method: to_openai_tool_schema() → dict
#       - Chuyển properties + required fields → OpenAI Function Calling schema format:
#         {"type": "function", "function": {"name": ..., "description": ..., "parameters": {...}}}
#
#     Abstract method:
#       async execute(**kwargs) → SkillResult
#
# LIBRARIES: abc, pydantic, typing
# =========================================================
