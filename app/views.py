import json, os
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


def index(request):
    context_dict = {"aboldmessage": "Description"}
    return render(request, "app/index.html", context=context_dict)


def gutty_response(request):
    msg = request.GET.get("msg", "").lower()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    try:
        with open(os.path.join(base_dir, "data", "storyline.json"), "r") as f:
            story = json.load(f)
    except FileNotFoundError:
        return JsonResponse({"response": "Error: storyline.json not found."})
    except json.JSONDecodeError:
        return JsonResponse({"response": "Error: storyline.json is not valid JSON."})

    scene = story.get("intro", {})
    reply = scene.get("text", "I'm not sure what to say about that.")
    
    return JsonResponse({"response": reply})
