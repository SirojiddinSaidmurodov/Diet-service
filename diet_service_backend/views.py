from django.http import JsonResponse
from django.shortcuts import render

from knowledge.diet_knowledgebase import get_dishes


def diet(request, query):
    results = get_dishes(query)
    return JsonResponse(results)
def index(request):
    return render(request,"base.html")