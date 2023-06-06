from django.http import HttpResponse
# from django.shortcuts import render
from .tasks import test_func
from send_email.tasks import send_email_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json

def test(request):
    test_func.delay()
    return HttpResponse("Done")

def send_email_to_all(request):
    send_email_func.delay()
    return HttpResponse("Sent")

def send_email_particular_time(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour = 18, minute = 15, day_of_month = 5, month_of_year = 6)
    task = PeriodicTask.objects.create(crontab = schedule, name = "schedule_email_task"+"2", task="send_email.tasks.send_email_func") #, args = json.dumps([[2,3]])) 
    return HttpResponse("Done")