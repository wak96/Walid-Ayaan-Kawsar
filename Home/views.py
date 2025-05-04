
from django.shortcuts import render
from . models import Clients, Work, Services

def home(request):
    client = Clients.objects.all()
    work = Work.objects.all()
    services = Services.objects.all()
    return render(request, 'index.html', {'clients':client,'works':work,'service':services})

