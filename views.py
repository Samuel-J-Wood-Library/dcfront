from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

def index(request):
    return HttpResponse("""<a href="info">Data Core Management</a>""")

class FrontPage(generic.TemplateView):
    template_name = 'dcfront/frontpage.html'

