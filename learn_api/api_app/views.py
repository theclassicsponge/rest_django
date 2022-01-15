from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from api_app.models import UserData
from api_app.serializers import ApiAppSerializer


def api_app_list(request):
    """
    List all users, or create a new user.
    """
    if request.method == 'GET':
        api_app = UserData.objects.all()
        serializer = ApiAppSerializer(api_app, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = ApiAppSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def api_app_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        api_app = UserData.objects.get(pk=pk)
    except api_app.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ApiAppSerializer(api_app)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        api_app = ApiAppSerializer(snippet, data=data)
        if api_app.is_valid():
            api_app.save()
            return JsonResponse(api_app.data)
        return JsonResponse(api_app.errors, status=400)

    elif request.method == 'DELETE':
        api_app.delete()
        return HttpResponse(status=204)
