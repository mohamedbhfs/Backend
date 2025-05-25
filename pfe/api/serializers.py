from rest_framework import serializers ;
from .models import Employe,Point_vente,Formulaire,Case,Visite,Position,Rapportvisite,Avertissement_retard

class Employeserializer(serializers.ModelSerializer):
    class Meta:
        model=Employe
        fields = '__all__'

class PointVenteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Point_vente
        fields = '__all__'
class FormulaireSerializer(serializers.ModelSerializer):
    class Meta:
        model=Formulaire
        fields = '__all__'
class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Case
        fields = '__all__'
class VisiteSerializer(serializers.ModelSerializer):
    nom_employe = serializers.CharField(source='Id_employe.Nom', read_only=True)
    nom_point_vente = serializers.CharField(source='Id_pos.Nom', read_only=True)
    class Meta:
        model=Visite
        fields = '__all__'
        extra_fields = ['nom_employe', 'nom_point_vente']
class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Position
        fields = '__all__'
class AvertissementRetardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Avertissement_retard
        fields = '__all__'

class PointVenteLastVisiteSerializer(serializers.ModelSerializer):
    last_visite = serializers.SerializerMethodField()

    class Meta:
        model = Point_vente
        fields = '__all__'  # ou ['id', 'nom', ..., 'last_visite']

    def get_last_visite(self, obj):
        visite = Visite.objects.filter(Id_pos=obj,Etat='Reussie').order_by('-Date').first()
        return visite.Date if visite else ""
class VisiteMarchandiseur(serializers.ModelSerializer):
        Id_pos = PointVenteLastVisiteSerializer()
        class Meta:
          model = Visite
          fields = '__all__'
class RapportvisiteSerializer(serializers.ModelSerializer):
    class Meta:
        model =Rapportvisite
        fields = '__all__'




    



    
