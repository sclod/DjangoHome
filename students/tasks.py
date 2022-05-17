from random import randrange
from time import sleep
from django.core.mail import send_mail

from celery import shared_task
from faker import Faker

from .models import Student


fake = Faker()


@shared_task
def create_random_students(total):
    result = []

    for i in range(total):
        result.append(Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            age=randrange(1,99)
        ))
    Student.objects.bulk_create(result)

    return f'{total} random students created with success!'

@shared_task
def email_send(title, message, email):
    send_mail(
        title,
        message,
        'support@prrte.com',
        [email])
    return None



