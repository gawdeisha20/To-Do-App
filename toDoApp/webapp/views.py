from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import task
from . serializers import taskSerializer

# Create your views here.
class taskList(APIView):

    def get(self, request):
        tasks = task.objects.all()
        serializer = taskSerializer(tasks, many=True)
        return Response(serializer.data)


    def post(self):
        pass