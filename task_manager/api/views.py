from rest_framework.response import Response
from rest_framework.decorators import api_view
from task.models import TaskItem
from rest_framework import status
from django.shortcuts import render,HttpResponse,redirect
from .serializers import TaskItemSerializer

@api_view(['GET'])
def getData(request):
    items = TaskItem.objects.all()
    serializer = TaskItemSerializer(items,many=True) 
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = TaskItemSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()  
    else:
        return Response(request.data)
    posts = TaskItem.objects.all()
    return redirect("/",{"posts":posts}) 

@api_view(['GET'])
def deleteItem(request):  
    item = TaskItem.objects.filter(id=request.GET["id"])
    item.delete()
    posts = TaskItem.objects.all()
    return redirect("/",{"posts":posts}) 

@api_view(["POST"])
def editItem(request):     
    try:
        item = TaskItem.objects.get(id=request.data.get("id"))
    except TaskItem.DoesNotExist:
        return Response({"error":"Item not found"},status= status.HTTP_404_NOT_FOUND)
    
    serialized_request = TaskItemSerializer(item,data=request.data)
    if(serialized_request.is_valid()):
        serialized_request.save()
        posts = TaskItem.objects.all()
        return redirect("/",{"posts":posts}) 
    else:
        return Response(serialized_request.errors,status = status.HTTP_400_BAD_REQUEST)