
from django.shortcuts import render
from .models import Persona, Portfolio


def home(request):
    persona = Persona.objects.first()

    return render(request, 'core/index.html', {
        'persona': persona
    })


def about(request):
    return render(request, 'core/about.html')


def portfolio(request):
    proyectos = Portfolio.objects.all()

    return render(request, 'core/portfolio.html', {
        'proyectos': proyectos
    })

def contact(request):
    return render(request, 'core/contact.html')