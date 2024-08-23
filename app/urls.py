from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('news', views.news, name='news'),
    path('characters', views.characters, name='characters'),
    path('character/<slug:slug>/', views.character, name='character'),

    path('lore', views.lore, name='lore'),
]