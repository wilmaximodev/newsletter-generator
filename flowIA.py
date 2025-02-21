from langflow.load import run_flow_from_json
from api.geminiAPI import GEMINI_API_KEY

def langflow_call(theme, url):
  TWEAKS = {
    "ParseData-8uEqG": {
      "sep": "\n",
      "template": "{text}"
    },
    "Prompt-WQuJl": {
      "template": "Escreva uma Newsletter baseada no link recebido\n\nTheme\n{theme}\n\n---\n\nURl\n{url}\n",
      "tool_placeholder": "",
      "theme": "",
      "url": ""
    },
    "TextInput-sUx5e": {
      "input_value": "Se baseie nos textos, seja lá qual for o assunto"
    },
    "ChatOutput-N8sAz": {
      "background_color": "",
      "chat_icon": "",
      "data_template": "{text}",
      "input_value": "",
      "sender": "Machine",
      "sender_name": "AI",
      "session_id": "",
      "should_store_message": True,
      "text_color": ""
    },
    "URL-AmkLo": {
      "format": "Text",
      "urls": [
        "https://langflow.org/",
        "https://docs.langflow.org/"
      ]
    },
    "GoogleGenerativeAIModel-y6wKa": {
      "api_key": "AIzaSyDMZaxFXfCWUe88-eiYDVBzRUKe5HfQd4g",
      "input_value": "",
      "max_output_tokens": None,
      "model_name": "gemini-1.5-flash",
      "n": None,
      "stream": False,
      "system_message": "",
      "temperature": 0.1,
      "tool_model_enabled": False,
      "top_k": None,
      "top_p": None
    }
  }

  TWEAKS["GoogleGenerativeAIModel-y6wKa"]["google_api_key"] = GEMINI_API_KEY
  TWEAKS["TextInput-sUx5e"]["input_value"] = theme
  TWEAKS["URL-AmkLo"]["urls"] = [url]

  result = run_flow_from_json(flow="./newsletter-generator.json",
                              session_id="", # provide a session id if you want to use session state
                              fallback_to_env_vars=True, # False by default
                              input_value="",
                              tweaks=TWEAKS)
  
  import pdb; pdb.set_trace()