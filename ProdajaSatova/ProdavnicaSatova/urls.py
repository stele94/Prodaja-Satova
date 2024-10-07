from django.urls import path
from . import views

app_name='prodavnicasatova'
urlpatterns = [
    path('', views.ListaSatova, name='ListaSatova'),
    path('tip/<slug:tip_slug>/', views.ListaSatovaPoTipu, name='ListaSatovaPoTipu'),
    path('kategorija/<slug:kategorija_slug>/', views.ListaSatovaPoKategoriji, name='ListaSatovaPoKategoriji'),
    path('brend/<slug:brend_slug>/', views.ListaSatovaPoBrendu, name='ListaSatovaPoBrendu'),
    path('<int:id>/<slug:slug>', views.DetaljiSata, name='DetaljiSata'),
]
