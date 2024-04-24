from rest_framework import serializers

from resources.models import Category, PeriodFilter, FilterCategories, Filters, Province, Resource, Interive, \
    Attributes, Contents


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'icon', 'order', ]


class PeriodFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodFilter
        fields = ['title', ]


class FilterCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilterCategories
        fields = ['title', 'category', ]


class FiltersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filters
        fields = ['filter_category', 'title', ]


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['title', ]


class InteriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interive
        fields = ['status', 'title', 'file', 'link', 'latitude', 'longitude']


class AttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attributes
        fields = ['resource_attribute', 'attributes_title', 'attributes_description', ]


class ContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contents
        fields = ['resource_content', 'contents_title', 'contents_description']


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['category', 'filter_category', 'filters', 'period_filter', 'title',
                  'image', 'content', 'statehood', 'province']
