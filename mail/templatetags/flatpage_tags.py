from django.template import Library
from django.contrib.flatpages.models import FlatPage

register = Library()

def get_pages():
    return {'pages':FlatPage.objects.order_by('-pk')[:5]}
    
register.inclusion_tag('pagelist.html')(get_pages)