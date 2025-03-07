from django.db import models
from django import forms

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel,  MultiFieldPanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from wagtail.search import index



class BlogIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]
    subpage_types = ['BlogPage','ViajesPage']

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')

        context['blogpages'] = blogpages
        
        return context

class BlogTagIndexPage(Page):
    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)
        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )
class ViajesTagIndexPage(Page):
    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        viajespages = ViajesPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['viajespages'] = viajespages
        return context
class ViajePageTag(TaggedItemBase):
    content_object = ParentalKey(
        'ViajesPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )



class BlogPage(Page):
    date = models.DateField("Fecha Post")
    intro = models.CharField("Introducción", max_length=250)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    parent_page_types = ['BlogIndexPage',]
    subpage_types = []
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),            
            ],
            heading='Información'
        ),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', 
            label="Galería de imágenes"),
    ]
    def imagen_blog(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None 

class ViajesPage(Page):
    date = models.DateField("Fecha Post")
    intro = models.CharField("Introducción", max_length=250)
    body = RichTextField(blank=True)
    coordenadas = models.CharField("coordenadas", blank=True, max_length=500)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    parent_page_types = ['BlogIndexPage']
    subpage_types = []


    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('coordenadas'),
            
            ],
            heading='Información'
        ),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', 
            label="Galería de imágenes"),
    ]
    def imagen_blog(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None 


class NoticiasIndexPage(Page):
    introduccion = RichTextField(blank=True)
    # pagina que servirá como índice para las noticias
    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]
    subpage_types = ['NoticiasPage']

    def get_context(self, request):
        context = super().get_context(request)
        noticiaspages = self.get_children().live().order_by('-first_published_at')
        context['noticiaspages'] = noticiaspages
        
        return context
    def noticias_list(context):
        noticias = NoticiasPage.objects.all().order_by('-date')
        return {
            'request': context['request'],
            'noticias': noticias
        }

class NoticiasPage(Page):
    date = models.DateField("Fecha Post")
    titulo = models.CharField("Titulo", max_length=250, blank=True)
    intro = models.CharField("Introducción", max_length=250)
    body = RichTextField(blank=True)    
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
            FieldPanel('titulo'),
            ImageChooserPanel("header_image"),
            InlinePanel('gallery_images', 
            label="Galería de imágenes"),
            ],
            
            heading='Información'
        ),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),

    ]
    def imagen_blog(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None 

class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, 
        on_delete=models.CASCADE, 
        related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

class NoticiasPageGalleryImage(Orderable):
    page = ParentalKey(NoticiasPage, 
        on_delete=models.CASCADE, 
        related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

class ViajesPageGalleryImage(Orderable):
    page = ParentalKey(ViajesPage, 
        on_delete=models.CASCADE, 
        related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categorías de blog'
        verbose_name = 'categoría de blog'

@register_snippet # añadimos a fragmentos el footer para poder editarlo desde el admin
class FooterText(models.Model):
    titulo = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Footer'



class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )



class ContactPage(AbstractEmailForm):

    template = "blog/contact/contact_page.html"
    # Esta será la pgina de contacto
    # y esta de debajo sera la de agradecimiento al enviarlo
    landing_page_template = "blog/contact/contact_page_landing.html"

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel("subject"),
        ], heading="Email Settings"),
    ]