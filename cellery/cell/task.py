from celery import shared_task
from time import sleep
from django.core.mail import send_mail


@shared_task
def sleepy(duariton):
    sleep(duariton)
    return None

@shared_task
def send_mail_task():
    send_mail(
    'Subject here',
    'Here is the message.',
    'nityanandabehera85132@gmail.com',
    ['shashwatsahu780@gmail.com'],
    fail_silently=False,
)
    return None