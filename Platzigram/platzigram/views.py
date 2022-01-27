"""Platzigram views"""

from django.http.response import HttpResponse

from datetime import datetime

def hello_world(request):
    """Return a greeting"""
    now = datetime.now()
    return HttpResponse(f'Oh, hi! Current server time is {now}')
