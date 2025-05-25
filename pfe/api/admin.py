from django.contrib import admin
from .models import Employe ,Point_vente,Formulaire,Visite,Case,Position
from django_celery_beat.models import PeriodicTask, IntervalSchedule

# Register your models here.
admin.site.register(Employe) 
admin.site.register(Point_vente)