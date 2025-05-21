import os
from google.genai import types


LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

API_VERSION = "1.1.1"
API_PREFIX = "/api/v1"

PROJECT_NAME = "zbala-1"
PROJECT_LOCATION = "global"
MODEL_NAME = "gemini-2.5-pro-preview-05-06"

CONTENT_CONFIG = types.GenerateContentConfig(
    temperature = 0.7,
    top_p = 1,
    max_output_tokens = 8192,
    safety_settings = [types.SafetySetting(
      category="HARM_CATEGORY_HATE_SPEECH",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_DANGEROUS_CONTENT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_HARASSMENT",
      threshold="OFF"
    )],
  )
