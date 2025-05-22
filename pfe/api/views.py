from django.shortcuts import render
from rest_framework import generics
import calendar
from datetime import date, timedelta
from django.http import HttpResponse
from .serializers import (
    Employeserializer,PointVenteSerializer, FormulaireSerializer, CaseSerializer, 
    VisiteSerializer, PositionSerializer, RepenseCaseSerializer, 
    AvertissementRetardSerializer,VisiteMarchandiseur,PointVenteLastVisiteSerializer
)
from .models import Point_vente, Formulaire, Case, Visite, Position, Repense_case, Avertissement_retard,Employe
from pfe.tasks import VerifieVisite
class Marchandiseurlistcreateapi(generics.ListCreateAPIView):
    queryset=Employe.objects.all().filter(Poste="Marchandiseur")
    serializer_class=Employeserializer

class Marchandiseurretrieve(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=Employeserializer
    def get_queryset(self):
        return Employe.objects.filter(Poste="Marchandiseur") 

# Point_Vente
class PointVentelistcreateapi(generics.ListCreateAPIView):
    queryset = Point_vente.objects.all()
    serializer_class = PointVenteSerializer

class PointVenteretrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Point_vente.objects.all()
    serializer_class = PointVenteSerializer

# Formulaire
class Formulairelistcreateapi(generics.ListCreateAPIView):
    queryset = Formulaire.objects.all()
    serializer_class = FormulaireSerializer

class Formularieretrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Formulaire.objects.all()
    serializer_class = FormulaireSerializer

# Case
class Caselistcreateapi(generics.ListCreateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

class Caseretrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

# Visite
class Visitelistcreateapi(generics.ListCreateAPIView):
    queryset = Visite.objects.all()
    serializer_class = VisiteSerializer

class Visiteretrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visite.objects.all()
    serializer_class = VisiteSerializer

# Position
class Positionlistcreateapi(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class Positionretrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

# Repense_case
class RepenseCaselistcreateapi(generics.ListCreateAPIView):
    queryset = Repense_case.objects.all()
    serializer_class = RepenseCaseSerializer

class RepenseCaseretrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Repense_case.objects.all()
    serializer_class = RepenseCaseSerializer

# Avertissement_retard
class AvertissementRetardlistcreateapi(generics.ListCreateAPIView):
    queryset = Avertissement_retard.objects.all()
    serializer_class = AvertissementRetardSerializer

class AvertissementRetardretrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avertissement_retard.objects.all()
    serializer_class = AvertissementRetardSerializer

#visite avec filtrage
class Filtervisite(generics.ListAPIView):
        serializer_class = VisiteSerializer
        def get_queryset(self):
            queryset = Visite.objects.all()
            nom_visite = self.request.query_params.get('nom_visite')
            point_vente = self.request.query_params.get('point_vente')
            marchandiseur = self.request.query_params.get('marchandiseur')
            etat = self.request.query_params.get('etat')
            dat = self.request.query_params.get('date')
            if(dat and dat.lower()=="audjord'hui"):
                queryset = queryset.filter(Date=date.today())
            elif(dat and dat.lower()=='cette semaine'):
                debut_semaine = date.today() - timedelta(days=(date.today().weekday() + 2) %7)
                fin_semaine = debut_semaine + timedelta(days=6)
                queryset=queryset.filter(Date__range=[debut_semaine, fin_semaine])
            elif(dat and dat.lower()=='ce mois'):
                annee_actuelle = date.today().year 
                mois_actuel = date.today().month
                dernier_jour = calendar.monthrange(annee_actuelle, mois_actuel)[1]
                debut_mois = date.today().replace(day=1)
                fin_mois = date.today().replace(day=dernier_jour)
                queryset=queryset.filter(Date__range=[debut_mois, fin_mois])
            if(etat and etat.lower()=='prevu'):
                queryset=queryset.filter(Etat='Prevu')
            elif(etat and etat.lower()=='en cours'):
                queryset=queryset.filter(Etat='En cours')
            elif(etat and etat.lower()=='termine'):
                queryset=queryset.filter(Etat='Reussie')
            if(nom_visite!=''):
                queryset=queryset.filter(Nom__icontains=nom_visite)   
            if(marchandiseur and marchandiseur.lower()=='true'):
                queryset=queryset.order_by('Id_employe__Nom')
            if(point_vente and point_vente.lower()=='true'):
                queryset=queryset.order_by('Id_pos__Nom')
            return queryset
class VisiteMarchandiseurlistapi(generics.ListAPIView):
    serializer_class = VisiteMarchandiseur
    def get_queryset(self):
        id_marchandiseur = 1 
        dat=self.request.query_params.get('date')
        etat=self.request.query_params.get('etat')
        queryset = Visite.objects.filter(Id_employe=id_marchandiseur)
        if(dat and dat.lower()=="audjord'hui"):
                queryset = queryset.filter(Date=date.today())
        elif(dat and dat.lower()=='cette semaine'):
                debut_semaine = date.today() - timedelta(days=(date.today().weekday() + 2) %7)
                fin_semaine = debut_semaine + timedelta(days=6)
                queryset=queryset.filter(Date__range=[debut_semaine, fin_semaine])
        elif(dat and dat.lower()=='ce mois'):
            annee_actuelle = date.today().year 
            mois_actuel = date.today().month
            dernier_jour = calendar.monthrange(annee_actuelle, mois_actuel)[1]
            debut_mois = date.today().replace(day=1)
            fin_mois = date.today().replace(day=dernier_jour)
            queryset=queryset.filter(Date__range=[debut_mois, fin_mois])
        if(etat and etat.lower()=='prevu'):
            queryset=queryset.filter(Etat='Prevu')
        else:
            queryset=queryset.filter(Etat='Termine')
        return queryset
class  Filterpointvente(generics.ListAPIView):
    serializer_class = PointVenteLastVisiteSerializer
    def get_queryset(self):
        nom_pos = self.request.query_params.get('nom_pos') or ""
        queryset=Point_vente.objects.filter(Nom__icontains=nom_pos)
        return queryset
class  FilterRapportEnable(generics.ListAPIView):
        serializer_class = VisiteMarchandiseur
        def get_queryset(self):
            id_March_Super = self.request.query_params.get('id')
            queryset=Visite.objects.filter(Id_employe=id_March_Super,Etat='Rapport en attente')
            return queryset
class FilterCases(generics.ListAPIView):
    serializer_class=CaseSerializer
    def get_queryset(self):
        Id_formulaire = self.request.query_params.get('Id_formulaire')
        queryset =Case.objects.filter(Id_formulaire=Id_formulaire)
        return queryset
        


















    







        

