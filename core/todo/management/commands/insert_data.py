from django.core.management.base import BaseCommand
from faker import Faker
from datetime import datetime
from django.contrib.auth import get_user_model
from todo.models import Task
import random

User = get_user_model()
class Command(BaseCommand):
    help = 'Inserting test data'
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()
    def handle(self, *args, **options):
        user = User.objects.create_user(username=self.fake.user_name(),password='test12345678@')
        for _ in range(10):
            Task.objects.create(
                user=user,
                title=self.fake.paragraph(nb_sentences=1),
                is_complete=random.choice([True,False]),
                updated_date=datetime.now()
            )