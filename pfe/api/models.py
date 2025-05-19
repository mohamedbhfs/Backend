from django.db import models

Postechoice=[
    ('Responsable Generale','Responsable Generale'),
    ('Responsable Marchandiseur','Responsable Marchandiseur'),
    ('Responsable Superviseur','Responsable Superviseur'),
    ('Marchandiseur','Marchandiseur'),
    ('Superviseur','Superviseur')
]
True_false_choices=[
    ('True','True'),
    ('False','False')
]
Etatchoice=[
    ('Prevu','Prevu'),
    ('En cours','En cours'),
    ('Termine','Termine'),
    ('Non Effectue','Non Effectue')
]

# Create your models here.
class Employe(models.Model):
    Nom = models.CharField(max_length=30)
    Prenom=models.CharField(max_length=30)
    Date_Naissance=models.DateField()
    Adresse=models.TextField()
    Poste=models.CharField(max_length=30,choices=Postechoice)
    Employe_non_Conforme=models.CharField(max_length=5,choices=True_false_choices)
    Employe_Suspendu=models.CharField(max_length=5,choices=True_false_choices)
    Nom_utilisateur=models.CharField(max_length=30,unique=True,null=True)
    Mote_passe=models.CharField(max_length=30,null=True)

class Point_vente(models.Model):
    Nom = models.CharField(max_length=30)
    Latitude=models.FloatField(null=True)
    Longtitude=models.FloatField(null=True)
    Adresse =models.TextField(null=True)
class Formulaire(models.Model):
    Version=models.IntegerField(primary_key=True)

class Case(models.Model):
    Information=models.TextField()
    Id_formulaire=models.ForeignKey(Formulaire,on_delete=models.CASCADE)

class Visite(models.Model):
    Nom=models.CharField(max_length=30)
    Date=models.DateField()
    Etat=models.CharField(max_length=20,choices=Etatchoice)
    Temp_arv_est_pos=models.TimeField(null=True)
    Temp_arv_reel_pos=models.TimeField(null=True)
    Problem=models.TextField(null=True)
    Arrive=models.CharField(max_length=5,choices=True_false_choices,null=True)
    Id_pos=models.ForeignKey(Point_vente,on_delete=models.CASCADE)
    Id_employe=models.ForeignKey(Employe,on_delete=models.CASCADE)
    Id_formulaire=models.ForeignKey(Formulaire,on_delete=models.CASCADE)


class Position(models.Model):
    Adresse=models.TextField()
    Heure_de_capture=models.TimeField()
    Id_visite=models.ForeignKey(Visite,on_delete=models.CASCADE,null=True)
    


class Repense_case(models.Model):
    Reponse=models.TextField()
    Id_case=models.ForeignKey(Case,on_delete=models.CASCADE)
    Id_visite=models.ForeignKey(Visite,on_delete=models.CASCADE)

class Avertissement_retard(models.Model):
    Avertissement=models.TextField()
    Id_Employe=models.ForeignKey(Employe,on_delete=models.CASCADE)


