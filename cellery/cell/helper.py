from django.shortcuts import render
from django.http import HttpResponse
from .task import *
from .helper import *
from django.core.mail import send_mail


def send_mail_without_celery():
    send_mail(
    'Subject here',
    'Here is the message.',
    'nityanandabehera85132@gmail.com',
    ['nityanandabehera85132@gmail.com'],
    fail_silently=False,
)
    return None