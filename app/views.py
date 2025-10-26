import json, os
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


def index(request):
    context_dict = {"aboldmessage": "Description"}
    # return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")
    return render(request, "app/index.html", context=context_dict)


def gutty_response(request):
    msg = request.GET.get("msg", "").lower()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(base_dir, "data", "storyline.json"), "r") as f:
        story = json.load(f)

    scene = story.get("intro")
    reply = scene["text"]

    if "hello" in msg:
        reply = "Hey coder! Ready to win GUTS 2025?"
    elif "project" in msg:
        reply = "We're picking the JPMorgan FinTech Challenge, obviously"
    elif "bye" in msg:
        reply = "Good luck! Don't forget your caffeine dose"
    else:
        reply = "Hmm… I don't get what your saying, you see! I'm still learning, but let's focus on the hackathon!"
    return JsonResponse({"response": reply})
