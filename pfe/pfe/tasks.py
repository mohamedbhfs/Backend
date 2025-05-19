from celery import shared_task
from api.models import Visite
from datetime import date

@shared_task
def VerifieVisite():
    count = Visite.objects.filter(Date__lt=date.today()).exclude(Etat='Termine').update(Etat='Non Effectue')
    return f"{count} visites mises à jour"