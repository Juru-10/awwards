from rest_framework import serializers
from .models import Profile,Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (id,prof_pic,bio,posts,contact)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (id,title,image,description,link,reviews)
