from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import task
from . serializers import taskSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
class taskList(APIView):

    def get(self, request):
        tasks = task.objects.all()
        serializer = taskSerializer(tasks, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = taskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        item = get_object_or_404(task, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
