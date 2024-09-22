from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(
        get_user_model(), null=True, blank=True, on_delete=models.CASCADE
    )

    title = models.CharField(max_length=250)
    is_complete = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    class Meta:
        order_with_respect_to = "user"

    def __str__(self):
        return self.title
