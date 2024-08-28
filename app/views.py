from django.shortcuts import get_object_or_404, render
from django.template.response import TemplateResponse

from .models import Character, Article


def index(request):
    context = {
        'articles': Article.objects.all()[:6]
    }
    return TemplateResponse(request, 'pages/index.html', context)


def news(request):
    context = {
        'articles': Article.objects.all()
    }
    return TemplateResponse(request, 'pages/news.html', context)


def article(request, article_id):
    context = {
        "article": get_object_or_404(Article, pk=article_id)
    }
    return TemplateResponse(request, 'pages/article_detail.html', context)


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
