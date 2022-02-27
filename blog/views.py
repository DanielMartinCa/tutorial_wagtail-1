from django.shortcuts import render
from django.views import generic
from noticias.models import NoticiasPage
# Create your views here.
class NoticiaDetailView(generic.DetailView):
    model = NoticiasPage
