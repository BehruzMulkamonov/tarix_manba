from rest_framework import viewsets

from admin_panel.serializer.resources import CategoryAdminSerializer, PeriodFilterAdminSerializer, \
    FilterCategoriesAdminSerializer, FiltersAdminSerializer, ProvinceAdminSerializer, ResourceAdminSerializer, \
    InteriveAdminSerializer, AttributesAdminSerializer, ContentsAdminSerializer
from resources.models import Category, FilterCategories, Filters, Province, Resource, Interive, Attributes, Contents


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryAdminSerializer





class PeriodFilterModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = PeriodFilterAdminSerializer


class FilterCategoriesModelViewSet(viewsets.ModelViewSet):
    queryset = FilterCategories.objects.all()
    serializer_class = FilterCategoriesAdminSerializer

class FiltersModelViewSet(viewsets.ModelViewSet):
    queryset = Filters.objects.all()
    serializer_class = FiltersAdminSerializer

class ProvinceModelViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceAdminSerializer


class ResourceModelViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceAdminSerializer


class InteriveModelViewSet(viewsets.ModelViewSet):
    queryset = Interive.objects.all()
    serializer_class = InteriveAdminSerializer

class AttributesModelViewSet(viewsets.ModelViewSet):
    queryset = Attributes.objects.all()
    serializer_class = AttributesAdminSerializer


class ContentsModelViewSet(viewsets.ModelViewSet):
    queryset = Contents.objects.all()
    serializer_class = ContentsAdminSerializer





