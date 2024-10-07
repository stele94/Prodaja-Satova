from django.db import models # type: ignore
from django.urls import reverse # type: ignore

# Create your models here.
class Tip(models.Model):
    naziv = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering = ('naziv',)
        verbose_name = 'tip'
        verbose_name_plural = 'tipovi'
    def __str__(self): return self.naziv
    def ApsolutniURL(self): return reverse('ProdavnicaSatova:ListaSatovaPoTipu', args=[self.slug])
    
class Kategorija(models.Model):
    naziv = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering = ('naziv',)
        verbose_name = 'kategorija'
        verbose_name_plural = 'kategorije'
    def __str__(self): return self.naziv
    def ApsolutniURL(self): return reverse('ProdavnicaSatova:ListaSatovaPoKategoriji', args=[self.slug])

class Brend(models.Model):
    naziv = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering = ('naziv',)
        verbose_name = 'brend'
        verbose_name_plural = 'brendovi'
    def __str__(self): return self.naziv
    def ApsolutniURL(self): return reverse('ProdavnicaSatova:ListaSatovaPoBrendu', args=[self.slug])

class Sat(models.Model):
    tip = models.ForeignKey(Tip, related_name='satovi', on_delete=models.CASCADE)    
    kategorija = models.ForeignKey(Kategorija, related_name='satovi', on_delete=models.CASCADE)
    brend = models.ForeignKey(Brend, related_name='satovi', on_delete=models.CASCADE)
    naziv = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    slika = models.ImageField(upload_to='satovi/%Y/%m/%d', blank=True)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    raspoloziv = models.BooleanField(default=True)
    kreiran = models.DateTimeField(auto_now_add=True)
    azuriran = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('naziv',)
        indexes = [
            models.Index(fields=['id', 'slug']), 
        ]
        verbose_name_plural = 'satovi'
    def __str__(self): return self.naziv
    def ApsolutniURL(self): return reverse('ProdavnicaSatova:DetaljiSata', args=[self.id, self.slug])
