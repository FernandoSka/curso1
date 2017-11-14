from django.http import HttpResponse
from apli.forms import UserCreation
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.views.generic import CreateView


import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

class fecha(TemplateView):
    template_name = "fecha.html"

class Registro(CreateView):
    form_class = UserCreation
    template_name = "registro.html"