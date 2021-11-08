from django.shortcuts import render
from django.http import HttpResponse
from .task import *
from .helper import *
from time import sleep
from django.core.mail import send_mail

def index(request):
     send_mail_task.delay()
     return HttpResponse("<h1>Hello</h1>")