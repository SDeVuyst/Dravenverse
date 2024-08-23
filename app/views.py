from django.shortcuts import render
from django.template.response import TemplateResponse

from .models import Character


def index(request):
    context = {}
    return TemplateResponse(request, 'pages/index.html', context)


def news(request):
    context = {}
    return TemplateResponse(request, 'pages/news.html', context)


def characters(request):
    context = {
        'characters': Character.objects.all()
    }
    return TemplateResponse(request, 'pages/characters.html', context)


def character(request, slug):
    character = Character.objects.get(slug=slug)
    context = {
        "character": character,
    }
    return TemplateResponse(request, 'pages/character-detail.html', context)


def lore(request):
    context = {}
    return TemplateResponse(request, 'pages/lore.html', context)
