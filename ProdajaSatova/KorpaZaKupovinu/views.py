from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from ProdavnicaSatova.models import Sat
from .korpa import Korpa
from .forms import FormaZaDodavanjSataUKorpu

# Create your views here.
@require_POST
def DodajUKorpu(request, sat_id):
    korpa = Korpa(request)
    sat = get_object_or_404(Sat, id=sat_id)
    form = FormaZaDodavanjSataUKorpu(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        korpa.Dodaj(sat=sat, kolicina=cd['kolicina'], dodati_na_kolicinu=cd['dodati_na_kolicinu'])
    return redirect('KorpaZaKupovinu:DetaljiKorpe')

@require_POST
def UkloniIzKorpe(request, sat_id):
    korpa = Korpa(request)
    sat = get_object_or_404(Sat, id=sat_id)
    korpa.Ukloni(sat)
    return redirect('KorpaZaKupovinu:DetaljiKorpe')

def DetaljiKorpe(request):
    korpa = Korpa(request)
    for stavka in korpa:
        stavka['formazaazuriranjekolicine'] = FormaZaDodavanjSataUKorpu(initial={'kolicina': 1, 'dodati_na_kolicinu': True})
    return render(request, 'KorpaZaKupovinu/detail.html', {'korpa': korpa})
