from django.urls import include, path
from .views import TaskList, TaskCreate, TaskComplete, TaskUpdate, TaskDelete

app_name = 'todo'

urlpatterns = [
    path("", TaskList.as_view(), name='task_list'),
    path("create/", TaskCreate.as_view(), name="create_task"),
    path("update/<int:pk>/", TaskUpdate.as_view(), name="update_task"),
    path("complete/<int:pk>/", TaskComplete.as_view(), name="complete_task"),
    path("delete/<int:pk>/", TaskDelete.as_view(), name="delete_task"),
    path('api/v1/', include('todo.api.v1.urls')),
]
