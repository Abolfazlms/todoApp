import pytest
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from todo.models import Task

User = get_user_model()


@pytest.mark.django_db
class TestTaskApi:
    def setup_method(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)

        # Create a sample task for testing
        self.task = Task.objects.create(title="Test Task", user=self.user)

    def test_list_tasks(self):
        url = reverse("todo:api-v1:todo-list")
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1  # Check that the task we created is returned

    def test_create_task(self):
        url = reverse("todo:api-v1:todo-list")
        data = {"title": "New Task"}
        response = self.client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Task.objects.count() == 2  # One from setup and one created here
        assert Task.objects.get(id=response.data["id"]).title == "New Task"

    def test_retrieve_task(self):
        url = reverse(
            "todo:api-v1:task-detail-detail", kwargs={"task_id": self.task.id}
        )
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["title"] == self.task.title

    def test_update_task(self):
        url = reverse(
            "todo:api-v1:task-detail-detail", kwargs={"task_id": self.task.id}
        )
        data = {"title": "Updated Task"}
        response = self.client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        self.task.refresh_from_db()
        assert self.task.title == "Updated Task"

    def test_delete_task(self):
        url = reverse(
            "todo:api-v1:task-detail-detail", kwargs={"task_id": self.task.id}
        )
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Task.objects.count() == 0  # The task should be deleted
