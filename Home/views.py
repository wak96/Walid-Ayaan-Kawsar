<<<<<<< HEAD

from django.shortcuts import render
from . models import Clients, Work, Services, Profile

def home(request):
    client = Clients.objects.all()
    work = Work.objects.all()
    services = Services.objects.all()
    profile = Profile.objects.first()
    return render(request, 'index.html', {'clients':client,'works':work,'service':services, 'profile':profile})

=======

from django.shortcuts import render
from . models import Clients, Work, Services, Profile

def home(request):
    client = Clients.objects.all()
    work = Work.objects.all()
    services = Services.objects.all()
    profile = Profile.objects.first()
    return render(request, 'index.html', {'clients':client,'works':work,'service':services, 'profile':profile})

>>>>>>> f64541b55aabf381935de6ce0c55bdd0bfee1421
