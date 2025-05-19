from django.urls import path,include
from .views import Marchandiseurlistcreateapi,Marchandiseurretrieve,PointVentelistcreateapi,PointVenteretrieve,Formulairelistcreateapi,Formularieretrieve,Visitelistcreateapi,Visiteretrieve,Filtervisite,VisiteMarchandiseurlistapi,Filterpointvente,testsend
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
    path('test/',testsend),


]