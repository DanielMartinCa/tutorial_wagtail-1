from blog.models import BlogCategory as Category
from django.template import Library, loader
from blog.models import FooterText
register = Library()


@register.inclusion_tag('blog/components/categories_list.html',
                        takes_context=True)
def categories_list(context):
    categories = Category.objects.all()
    return {
        'request': context['request'],
        'categories': categories
    }
@register.inclusion_tag('blog/components/footer_text.html', takes_context=True)
def get_footer_text(context):
    footer_text = ""
    if FooterText.objects.first() is not None:
        footer_text = FooterText.objects.first().titulo
    return {
        'footer_text': footer_text,
    }
