import django_filters
from .models import category,item


class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = category
        fields ='__all__'

class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = item
        fields =['name','category','unit']
       