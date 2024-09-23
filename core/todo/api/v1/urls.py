# from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = "api-v1"
router = DefaultRouter()
router.register("todo", views.TaskListViewSet, basename="todo")
router.register("task-detail", views.TaskDetailViewSet, basename="task-detail")
urlpatterns = router.urls

# urlpatterns = [
#     path('todo/',views.TaskListViewSet, name='todo-view'),
#     path('todo/<int:id>',views.TaskListViewSet,name='model')
# ]
# router.register('category',views.CategoryModelViewSet,basename='category')
