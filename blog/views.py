from django.shortcuts import render
from django.views import generic
from blog.models import NoticiasPage
from home.models import HomePage
# Create your views here.
class NoticiaDetailView(generic.DetailView):
    model = NoticiasPage


def lista_noticias(context):
    noticias = NoticiasPage.objects.all()
    context={'noticias':noticias}
    return context
    