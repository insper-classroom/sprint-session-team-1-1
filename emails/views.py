from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_func

def test(request):
    test_func.delay()
    return HttpResponse("Done")
