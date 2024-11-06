# myapp/vertex_ai_utils.py

import vertexai
from vertexai.generative_models import GenerativeModel, SafetySetting


def multiturn_generate_content(prompt_text):
    # Inicializa Vertex AI
    vertexai.init(project="test-projects-440617", location="us-central1")

    # Configura el modelo generativo
    model = GenerativeModel("gemini-1.5-flash-002")
    chat = model.start_chat()

    # Configuración de generación y seguridad
    generation_config = {
        "max_output_tokens": 512,
        "temperature": 0.7,
        "top_p": 0.9,
    }

    safety_settings = [
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
    ]

    # Genera el contenido usando Vertex AI
    response = chat.send_message(
        [prompt_text],
        generation_config=generation_config,
        safety_settings=safety_settings
    )

    return response.text
