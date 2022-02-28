

from django.db import models
from django import forms

from blog.models import BlogIndexPage, BlogTagIndexPage, NoticiasIndexPage, NoticiasPage


from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel



class HomePage(Page):
    body = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    subpage_types = ['blog.BlogIndexPage','blog.NoticiasIndexPage','blog.BlogTagIndexPage','blog.NoticiasPage']


    
