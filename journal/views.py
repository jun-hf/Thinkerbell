from django.shortcuts import render
from .models import Log

# Create your views here.

def home(req):
    return render(req, 'journal/home.html')

def log_list(req):
    logs = Log.objects.order_by('date_added')
    context = {'logs': logs}

    return render(req, 'journal/log.html', context)

def log(req):
    pass
