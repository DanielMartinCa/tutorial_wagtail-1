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



# Create your models here.

class NoticiasIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]
    subpage_types = ['NoticiasPage']
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        noticiaspages = self.get_children().live().order_by('-first_published_at')
        context['noticiaspages'] = noticiaspages
        
        return context

class NoticiasPage(Page):
    date = models.DateField("Fecha Post")
    intro = models.CharField("Introducción", max_length=250)
    body = RichTextField(blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)
    header_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    parent_page_types = [NoticiasIndexPage]
    subpage_types = []

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
            ImageChooserPanel("header_image"),
            ],
            heading='Información'
        ),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),

    ]
