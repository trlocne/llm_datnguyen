# frontend/src/components/model-selector.tsx
# =========================================================
# PURPOSE: UI panel cho phép thay đổi LLM provider, model, và sampling params.
#
# WHAT TO IMPLEMENT:
#   Props:
#     currentModel, baseUrl, temperature: number
#     availableModels: ModelOption[]
#     onModelChange, onBaseUrlChange, onTemperatureChange: callbacks
#
#   Render:
#     1. Dropdown <select> cho model_name (loop qua availableModels)
#     2. Text input cho base_url (placeholder: https://api.openai.com/v1)
#     3. Range slider temperature 0.0 → 1.0 step=0.05, hiện giá trị bên cạnh
#
#   Preset buttons: "OpenAI", "DeepSeek", "Groq", "Local Ollama"
#     → Mỗi button tự set baseUrl + model tương ứng (convenience shortcuts)
#
# LIBRARIES: React, lucide-react (Settings2, Cpu, Globe, Sliders icons)
# =========================================================
