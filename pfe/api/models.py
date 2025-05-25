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
    ('Rapport en attente', 'Rapport en attente'),
    ('Non Effectue','Non Effectue')
]
ReponseChoice=[
    ('Number','Number'),
    ('Boolean','Boolean'),
    ('Text','Text'),
]
Typevisitechoice =[
    ('Planifie','Planifie'),
    ('Libre','Libre'),
]
MarchSuperchoice=[
    ('Marchandiseur','Marchandiseur'),
    ('Superviseur','Superviseur'),
]

# Create your models here.
class Employe(models.Model):
    Nom = models.CharField(max_length=30)
    Prenom=models.CharField(max_length=30)
    Date_Naissance=models.DateField()
    Adresse=models.TextField()
    Poste=models.CharField(max_length=30,choices=Postechoice)
    Nom_utilisateur=models.CharField(max_length=30,unique=True,null=True)
    Mote_passe=models.CharField(max_length=30,null=True)

class Point_vente(models.Model):
    Nom = models.CharField(max_length=30)
    Adresse =models.TextField(null=True)
class Distributeur(models.Model):
    Nom = models.CharField(max_length=30)
    Adresse =models.TextField(null=True)
class Formulaire(models.Model):
    Version=models.IntegerField(primary_key=True)
    FormulaireMarchSuper=models.TextField(null=True,choices=MarchSuperchoice)
class Case(models.Model):
    Question=models.TextField(null=True)
    Id_formulaire=models.ForeignKey(Formulaire,on_delete=models.CASCADE)
    Type_reponse=models.TextField(choices=ReponseChoice,null=True)


class Visite(models.Model):
    Nom=models.CharField(max_length=30)
    Date=models.DateField()
    Etat=models.CharField(max_length=20,choices=Etatchoice)
    Temp_arv_est_pos=models.TimeField(null=True)
    Temp_arv_reel_pos=models.TimeField(null=True)
    VisiteMarchSuper=models.TimeField(null=True,choices=MarchSuperchoice)
    Problemes=models.TextField(null=True)
    Infomationssupplementaires=models.TextField(null=True)
    Type=models.CharField(max_length=20,choices=Typevisitechoice,null=True)
    Id_pos=models.ForeignKey(Point_vente,on_delete=models.CASCADE)
    Id_employe=models.ForeignKey(Employe,on_delete=models.CASCADE)
    Id_formulaire=models.ForeignKey(Formulaire,on_delete=models.CASCADE,null=True)

class Position(models.Model):
    Adresse=models.TextField()
    Heure_de_capture=models.TimeField()
    Id_visite=models.ForeignKey(Visite,on_delete=models.CASCADE,null=True)
    


class Rapportvisite(models.Model):
    url_file=models.URLField(null=True)
    Id_visite=models.ForeignKey(Visite,on_delete=models.CASCADE)

class Avertissement_retard(models.Model):
    Avertissement=models.TextField()
    Date=models.DateField(null=True)
    Id_Employe=models.ForeignKey(Employe,on_delete=models.CASCADE)
    
