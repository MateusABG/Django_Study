from django.shortcuts import render,HttpResponse
from .models import TaskItem,LoginItem
from api.serializers import TaskItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def create_post(request):   
    return render(request,"create_task.html")

def home(request): 
    posts = TaskItem.objects.all()
    return render(request,"home.html",{"posts":posts})

@api_view(['GET'])
def edit_post(request):  
    items = TaskItem.objects.filter(id=request.GET["id"])  
    return render(request,"edit_task.html",{"post":items[0]})

@api_view(["GET"])
def see_more(request):
    items = TaskItem.objects.filter(id=request.GET["id"])
    return render(request,"see_more.html",{"post":items[0]})