# myapp/views.py

from django.shortcuts import render
from .vertex_ai_utils import multiturn_generate_content
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def generate_content_view(request):
    response_text = ""

    if request.method == "POST":
        prompt_text = request.POST.get("prompt_text")
        if prompt_text:
            # Llama a la función de Vertex AI con el texto ingresado por el usuario
            response_text = multiturn_generate_content(prompt_text)

    # Renderiza la plantilla con la respuesta
    return render(request, 'generate_content.html', {'response_text': response_text})
