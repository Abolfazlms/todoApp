from rest_framework import serializers
from todo.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ['id','title','is_complete','created_date','updated_date']
        fields = "__all__"
