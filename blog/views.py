from django.shortcuts import render
from django.views import generic
from blog.models import NoticiasPage
# Create your views here.
class NoticiaDetailView(generic.DetailView):
    model = NoticiasPage
