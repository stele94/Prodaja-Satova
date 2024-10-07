from django.contrib import admin
from .models import Tip, Kategorija, Brend, Sat

# Register your models here.
@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):
    list_display = ['naziv', 'slug']
    prepopulated_fields = {'slug': ('naziv',)}

@admin.register(Kategorija)
class Kategorija(admin.ModelAdmin):
    list_display = ['naziv', 'slug']
    prepopulated_fields = {'slug': ('naziv',)}

@admin.register(Brend)
class Brend(admin.ModelAdmin):
    list_display = ['naziv', 'slug']
    prepopulated_fields = {'slug': ('naziv',)}

@admin.register(Sat)
class SatAdmin(admin.ModelAdmin):
    list_display = ['naziv', 'slug', 'cena', 'raspoloziv', 'kreiran', 'azuriran']
    list_filter = ['raspoloziv', 'kreiran', 'azuriran']
    list_editable = ['cena', 'raspoloziv']
    prepopulated_fields = {'slug': ('naziv',)}