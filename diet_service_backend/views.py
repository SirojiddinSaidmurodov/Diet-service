from django.http import JsonResponse
from django.shortcuts import render

from knowledge.diet_knowledgebase import process


def diet(request, query):
    results = process(query)
    return JsonResponse(results)


def index(request):
    return render(request, "base.html")
