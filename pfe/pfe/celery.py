import os
from celery import Celery
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pfe.settings')
app = Celery('pfe')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
@app.task(bind=True)
def VerifieVisite(arg):
    from api.models import Visite
    from django.db.models import Q
    count = Visite.objects.filter(Q(Date__lt=date.today()) & Q(Etat='Prevu') | Q(Etat='En cours')).update(Etat='Non Effectue')
    return f"{count} visites mises à jour"
