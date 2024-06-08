from rest_framework import serializers
from task.models import TaskItem

class TaskItemSerializer(serializers.ModelSerializer):
    class Meta: 
        model = TaskItem
        fields = '__all__' 