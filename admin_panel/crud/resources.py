from rest_framework import viewsets

from admin_panel.serializer.resources import CategorySerializer, PeriodFilterSerializer, FilterCategoriesSerializer, \
    FiltersSerializer, ProvinceSerializer, ResourceSerializer, InteriveSerializer, AttributesSerializer, \
    ContentsSerializer
from resources.models import Category, FilterCategories, Filters, Province, Resource, Interive, Attributes, Contents


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PeriodFilterModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = PeriodFilterSerializer


class FilterCategoriesModelViewSet(viewsets.ModelViewSet):
    queryset = FilterCategories.objects.all()
    serializer_class = FilterCategoriesSerializer

class FiltersModelViewSet(viewsets.ModelViewSet):
    queryset = Filters.objects.all()
    serializer_class = FiltersSerializer

class ProvinceModelViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


class ResourceModelViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class InteriveModelViewSet(viewsets.ModelViewSet):
    queryset = Interive.objects.all()
    serializer_class = InteriveSerializer

class AttributesModelViewSet(viewsets.ModelViewSet):
    queryset = Attributes.objects.all()
    serializer_class = AttributesSerializer


class ContentsModelViewSet(viewsets.ModelViewSet):
    queryset = Contents.objects.all()
    serializer_class = ContentsSerializer





