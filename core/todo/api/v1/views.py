from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .serializer import TaskSerializer
from todo.models import Task

class TaskListViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self, *args, **kwargs):
        return (super().get_queryset(*args, **kwargs).filter(user=self.request.user))
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

   
class TaskDetailViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    lookup_field = 'task_id'
    def get_object(self, queryset=None):
        object = Task.objects.get(pk=self.kwargs['task_id'])
        return object

    def delete(self, request, *args, **kwargs):
        task =self.get_object()
        task.delete()
        return Response({"detail": "Task successfully deleted."})
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    
    def post(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = TaskSerializer(
            data = request.data, instance=task, many=False
        )
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
