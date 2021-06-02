# from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<html><body>Olá Mundo</body></html>', content_type='text/html')
