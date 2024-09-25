from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializer import TaskSerializer
from todo.models import Task

import requests
from django.core.cache import cache
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

class TaskListViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetailViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    lookup_field = "task_id"

    def get_object(self, queryset=None):
        object = Task.objects.get(pk=self.kwargs["task_id"])
        return object

    def delete(self, request, *args, **kwargs):
        task = self.get_object()
        task.delete()
        return Response({"detail": "Task successfully deleted."})

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = TaskSerializer(data=request.data, instance=task, many=False)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class WeatherViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60 * 20)) # seconds * number
    @method_decorator(vary_on_cookie)
    def retrieve(self, request):
        city = 'Tehran'
        cached_data = cache.get(f'weather_data_{city}')
        if cached_data:
            return Response(cached_data)

        api_key = settings.OPENWEATHER_API_KEY
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            cache.set(f'weather_data_{city}', data, timeout=60 * 20)
            return Response(data)
        else:
            return Response({'error': 'Could not retrieve weather data'}, status=500)