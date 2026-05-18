from django.contrib import admin
from .models import Persona, Portfolio


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = (
        'nombres',
        'apellidos',
        'correo_electronico',
        'telefono'
    )


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('titulo',)