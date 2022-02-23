from django.db import models
from django import forms

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel,  MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
    
    def get_context(self, request):
        context = super().get_context(request)
        noticiaspages = self.get_children().live().order_by('-first_published_at')
        context['noticiaspages'] = noticiaspages
        
        return context

class NoticiasPage(Page):
    date = models.DateField("Fecha Noticia")
    intro = models.CharField("Titular", max_length=250)
    body = RichTextField(blank=True)

    parent_page_types = [HomePage]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            ],
        ),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),            
    ]
    
