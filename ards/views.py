from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Profile,Project
from .serializer import ProjectSerializer,ProfileSerializer

class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)
