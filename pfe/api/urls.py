from django.urls import path,include
from .views import Marchandiseurlistcreateapi,Marchandiseurretrieve,RepenseCaselistcreateapi,RepenseCaseretrieve,PointVentelistcreateapi,PointVenteretrieve,Formulairelistcreateapi,Formularieretrieve,Visitelistcreateapi,Visiteretrieve,Filtervisite,VisiteMarchandiseurlistapi,Filterpointvente,FilterRapportEnable,Formularieretrieve,FilterCases,Caselistcreateapi
urlpatterns =[
    path('listaddmarchandiseur/',Marchandiseurlistcreateapi.as_view()),
    path('marchandiseur/<int:pk>',Marchandiseurretrieve.as_view()),
    path('filtervisite/',Filtervisite.as_view()),
    path('listaddvisite/',Visitelistcreateapi.as_view()),
    path('visite/<int:pk>/',Visiteretrieve.as_view()),
    path('listaddformulaire/',Formulairelistcreateapi.as_view()),
    path('Visitemarchandiseur/',VisiteMarchandiseurlistapi.as_view()),
    path ('filterpointvente/',Filterpointvente.as_view()),
    path('Pointvente/<int:pk>/',PointVenteretrieve.as_view()),
    path('listaddpointvente/',PointVentelistcreateapi.as_view()),
    path('filterRapportEnable/',FilterRapportEnable.as_view()),
    path('filtercase/',FilterCases.as_view()),
    path('listaddcase/',Caselistcreateapi.as_view()),
    path('listaddrepensecase/',RepenseCaselistcreateapi.as_view()),

]