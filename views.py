from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("""<a href="info">Data Core Management</a>""")