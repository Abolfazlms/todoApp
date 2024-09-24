from celery import shared_task
from .models import Task

@shared_task
def delete_completed_tasks():
    obj = Task.objects.filter(is_complete=True)
    obj.delete()
    print('tasks are deleted.')
