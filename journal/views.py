from django.shortcuts import render, redirect
from .models import Entry, Log
from .forms import LogForm, EntryForm

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

def new_entry(req, log_id):
    log = Log.objects.get(id=log_id)

    if req.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=req.data)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.log = log
            new_entry.save()

            return redirect('log_detail', log_id=log_id)
    
    context = {'log': log, 'form': form}
    return render(req, 'journal/new_entry.html', context)

def edit_entry(req, entry_id):
    entry = Entry.objects.get(id=entry_id)
    log = entry.log 

    if req.method != "POST":
        form = EntryForm(instance=entry)

    else:
        form = EntryForm(instance=entry, data=req.POST)
        if form.is_valid():
            form.save() 
            return redirect('log_detail', log_id=log.id)
        
    context = {'entry': entry, 'log': log, 'form': form}
    return render(req, 'journal/edit_entry.html', context)
    