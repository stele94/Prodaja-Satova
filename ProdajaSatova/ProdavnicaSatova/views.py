from django.shortcuts import render, get_object_or_404
from .models import Tip, Kategorija, Brend, Sat
from KorpaZaKupovinu.korpa import Korpa
from KorpaZaKupovinu.forms import FormaZaDodavanjSataUKorpu

# Create your views here.
def ListaSatova(request, tip_slug=None, kategorija_slug=None, brend_slug=None):
    tip = None
    tipovi = Tip.objects.all()
    kategorija = None
    kategorije = Kategorija.objects.all()
    brend = None
    brendovi = Brend.objects.all()
    satovi = Sat.objects.filter(raspoloziv=True)

    if tip_slug:
        tip = get_object_or_404(Tip, slug=tip_slug)
        satovi = satovi.filter(tip=tip)
    
    if kategorija_slug:
        kategorija = get_object_or_404(Kategorija, slug=kategorija_slug)
        satovi = satovi.filter(kategorija=kategorija)

    if brend_slug:
        brend = get_object_or_404(Brend, slug=brend_slug)
        satovi = satovi.filter(brend=brend)
    
    korpa = Korpa(request)
    return render(request, 'ProdavnicaSatova/sat/list.html', {'tip': tip, 
                                                              'tipovi': tipovi, 
                                                              'kategorija':kategorija, 
                                                              'kategorije': kategorije, 
                                                              'brend':brend, 
                                                              'brendovi': brendovi, 
                                                              'satovi':satovi, 
                                                              'korpa': korpa})

def ListaSatovaPoTipu(request, tip_slug=None):
    return ListaSatova(request, tip_slug=tip_slug)

def ListaSatovaPoKategoriji(request, kategorija_slug=None):
    return ListaSatova(request, kategorija_slug=kategorija_slug)

def ListaSatovaPoBrendu(request, brend_slug=None):
    return ListaSatova(request, brend_slug=brend_slug)


def DetaljiSata(request, id, slug):
    sat = get_object_or_404(Sat, id=id, slug=slug, raspoloziv=True)
    korpa = Korpa(request)
    formazadodavanjesataukorpu = FormaZaDodavanjSataUKorpu()


    return render(request, 'ProdavnicaSatova/sat/detail.html', {'sat':sat,
                                                                'korpa': korpa,
                                                                'formazadodavanjesataukorpu': formazadodavanjesataukorpu})

