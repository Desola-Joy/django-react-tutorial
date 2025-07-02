from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions, status
from .serializers import *
from rest_framework.response import Response
from .models import *

def home(request):
    return HttpResponse("This is the homepage")


class ProjectViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def list(self, request):
        queryset = self.queryset 
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 201 on success
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 400 on validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # serializer = self.serializer_class(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors, status=404)

    def retrieve(self, request, pk=None):
        Project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(Project)
        return Response(serializer.data)

    def update(self, request, pk=None):
        Project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(Project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=404)


    def destroy(self, request, pk=None):
        Project = self.queryset.get(pk=pk)
        Project.delete()
        return Response(status=204)