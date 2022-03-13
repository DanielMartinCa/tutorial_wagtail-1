from django.db import models
from wagtail.core.models import Page 
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class PersonalEmpresa(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    nombre = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250)    
    email = models.CharField(max_length=250)
    genero = models.CharField(max_length=250)
    departamento = models.CharField(max_length=250)


    panels = [
        FieldPanel('id'),
        FieldPanel('nombre'),
        FieldPanel('apellidos'),
        FieldPanel('email'),
        FieldPanel('genero'),
        FieldPanel('departamento'),


    ]


    def __str__(self):
        return f'{self.nombre} ({self.apellidos})'
    
    class Meta:
        verbose_name = 'Personal de empresa'

class PersonalEmpresaIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def paginate(self, request, personal, *args):
        page = request.GET.get('page')
        
        paginator = Paginator(personal, 5)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages

    def get_context(self, request):
        context = super().get_context(request)
        context['personal'] =PersonalEmpresa.objects.all().order_by("apellidos")
        return context