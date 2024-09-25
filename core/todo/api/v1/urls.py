from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = "api-v1"
router = DefaultRouter()
router.register("todo", views.TaskListViewSet, basename="todo")
router.register("task-detail", views.TaskDetailViewSet, basename="task-detail")
router.register("weather", views.WeatherViewSet, basename="weather-api")
# urlpatterns = router.urls

urlpatterns = [
    path("weather/", views.WeatherViewSet.as_view({"get": "retrieve"}), name="weather"),
    path("", include(router.urls)),
]

# urlpatterns = [
#     path('todo/',views.TaskListViewSet, name='todo-view'),
#     path('todo/<int:id>',views.TaskListViewSet,name='model')
# ]
# router.register('category',views.CategoryModelViewSet,basename='category')
