from django.http import JsonResponse

from knowledge.diet_knowledgebase import get_dishes


def diet(request, query):
    results = get_dishes(query)
    return JsonResponse(results)
