from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import Clients, Work, Services
# Register your models here.


admin.site.register(Clients)
admin.site.register(Work)
admin.site.register(Services)