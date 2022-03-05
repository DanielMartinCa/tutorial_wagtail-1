

from django.db import models
from django import forms

from blog.models import BlogIndexPage, BlogTagIndexPage, NoticiasIndexPage, NoticiasPage
from personalempresa.models import PersonalEmpresaIndexPage

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel



class HomePage(Page):
    body = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
 
        noticiaspages = NoticiasPage.objects.all().order_by('-first_published_at')[:5]
        context['noticiaspages'] = noticiaspages
        
        return context
    subpage_types = ['blog.BlogIndexPage','blog.NoticiasIndexPage','blog.BlogTagIndexPage','blog.NoticiasPage']


    
