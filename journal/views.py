from django.shortcuts import render, redirect
from .models import Entry, Log
from .forms import LogForm

# Create your views here.

def home(req):
    return render(req, 'journal/home.html')

def log_list(req):
    logs = Log.objects.order_by('date_added')
    context = {'logs': logs}

    return render(req, 'journal/log.html', context)

def log_detail(req, log_id):
    log = Log.objects.get(id=log_id)
    entries = Entry.objects.filter(log=log)
    context = {'log': log, 'entries': entries}

    return render(req, 'journal/log_detail.html', context)

def new_log(req):
    if req.method != 'POST':
        form = LogForm()
    else:
        form = LogForm(data=req.POST)
        if form.is_valid():
            form.save()
            return redirect('log')

    context = { 'form': form}
    return render(req, 'journal/new_log.html', context)