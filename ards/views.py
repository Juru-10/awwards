from django.shortcuts import render,redirect

from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.contrib.auth.decorators import login_required
from .forms import NewProfForm, NewProjectForm, ReviewForm

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Profile,Project,Review,User
from .serializer import ProjectSerializer,ProfileSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly

@login_required(login_url='/accounts/login')
def home(request):
    try:
        date = dt.date.today()
        projects = Project.objects.all()
    except DoesNotExist:
        raise Http404()
    return render(request,"all_posts/home.html",{"date": date, "projects": projects})

@login_required(login_url='/accounts/login')
def prof(request):
    users =User.objects.all()

    for user in users:
        user=user
        profile = Profile.objects.all()
        projects = Project.objects.all()
        print(user)
    return render(request,"all_posts/prof.html",{ "user": user,"profile": profile,"projects": projects})

@login_required(login_url='/accounts/login')
def project(request,id):
    project = Project.objects.filter(id__icontains = id)
    return render(request,"all_posts/project",{"project": project})

@login_required(login_url='/accounts/login')
def search(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_project(search_term)
        message = f"{search_term}"
        return render(request,"all_posts/search.html", {"message": message, "projects": searched_projects})
    else:
        message = "There is no such project title"
        return render(request,"all_posts/search.html", {"message": message})

@login_required(login_url='/accounts/login')
def new_prof(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfForm(request.POST,request.FILES)
        print(form.errors.as_text())
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            # profile=Profile.objects.update()
            profile.save()
        return redirect('prof')
    else:
        form = NewProfForm()
    return render(request,'registration/new_prof.html',{"form": form,"id":id})

@login_required(login_url='/accounts/login')
def new_project(request):
    current_user=request.user
    profile= Profile.objects.filter(user=current_user.id).first()
    if request.method == 'POST':
        form = NewProjectForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile=profile
            project.save()
        return redirect('prof')
    else:
        form = NewProjectForm()
    return render(request,'registration/new_project.html',{"form": form,"id":id})

@login_required(login_url='/accounts/login')
def new_review(request):
    current_user=request.user
    profile= Profile.objects.filter(user=current_user.id).first()
    project= Project.objects.filter(profile=profile.id).first()
    if request.method == 'POST':
        form = ReviewForm(request.POST,request.FILES)
        # print(form.errors.as_text())
        if form.is_valid():
            review = form.save(commit=False)
            review.project=project
            review.save()
        return redirect('prof')
    else:
        form = ReviewForm()
    return render(request,'registration/review.html',{"form": form})

@login_required(login_url='/accounts/login/')
def admin(request):
    return render(request)

@login_required(login_url='/accounts/login/')
def delete(request,id):
    project = Project.objects.filter(id=id)
    project.delete()
    return redirect('prof')







class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        permission_classes = (IsAdminOrReadOnly,)

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        permission_classes = (IsAdminOrReadOnly,)

class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_project(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_project(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_profile(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_profile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
