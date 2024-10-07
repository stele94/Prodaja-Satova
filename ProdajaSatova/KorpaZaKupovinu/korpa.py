from decimal import Decimal
from django.conf import settings
from ProdavnicaSatova.models import Sat

class Korpa(object):
    def __init__(self, request):
        self.sesija = request.session
        korpa = self.sesija.get(settings.KORPA_ZA_KUPOVINU_SESSION_KEY)

        if not korpa:
            korpa = self.sesija[settings.KORPA_ZA_KUPOVINU_SESSION_KEY] = {}
        self.korpa = korpa

    def __iter__(self):
        satovi_ids = self.korpa.keys()
        satovi = Sat.objects.filter(id__in=satovi_ids)
        korpakopija = self.korpa.copy()
        for sat in satovi:
            korpakopija[str(sat.id)]['sat'] = sat
        for stavka in korpakopija.values():
            stavka['cena'] = Decimal(stavka['cena'])
            stavka['ukupna_cena'] = stavka['cena'] * stavka['kolicina']
            yield stavka

    def __len__(self):
        return sum(stavka['kolicina'] for stavka in self.korpa.values())
    
    def Dodaj(self, sat, kolicina=1, dodati_na_kolicinu=True):
        sat_id = str(sat.id)
        if sat_id not in self.korpa:
            self.korpa[sat_id] = {'kolicina':0, 'cena':str(sat.cena)}
        if dodati_na_kolicinu:
            self.korpa[sat_id]['kolicina'] += kolicina
        else:
            self.korpa[sat_id]['kolicina'] = kolicina
        self.sesija.modified = True
    
    def Ukloni(self, sat):
        sat_id = str(sat.id)
        if sat_id in self.korpa:
            del self.korpa[sat_id]
            self.sesija.modified = True
    
    def ObrisiJeIzSesije(self):
        del self.sesija[settings.KORPA_ZA_KUPOVINU_SESSION_KEY]
        self.sesija.modified = True

    def UzmiUkupnuCenu(self):
        return sum(Decimal(stavka['cena']) * stavka['kolicina'] for stavka in self.korpa.values())
        