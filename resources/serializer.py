from rest_framework import serializers

from admin_panel.serializer.resources import ResourceAdminSerializer
from resources.models import Category, PeriodFilter, FilterCategories, Filters, Province, Resource, Interive, \
    Attributes, Contents




class PeriodFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodFilter
        fields = ['id','title', ]


class FilterCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilterCategories
        fields = ['id','title', 'category', ]


class FiltersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filters
        fields = ['id','filter_category', 'title', ]


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['id','title', ]


class InteriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interive
        fields = ['id','status', 'title', 'file', 'link', 'latitude', 'longitude']


class AttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attributes
        fields = ['id','resource_attribute', 'attributes_title', 'attributes_description', ]


class ContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contents
        fields = ['id','resource_content', 'contents_title', 'contents_description']


class ResourceSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    filter_category_title = serializers.SerializerMethodField()
    # filters_title = serializers.SerializerMethodField()

    class Meta:
        model = Resource
        fields = ['category', 'filter_category', 'filters', 'period_filter', 'title',
                  'image', 'content', 'statehood', 'province','category_name',
                  'filter_category_title',]

    def get_category_name(self, obj):
        return obj.category.title

    def get_filter_category_title(self, obj):
        filter_category=obj.filter_category
    #
    #     if filter_category:
    #         filter_category_obj=Category.objects.filter(title=filter_category.category)
    #         return filter_category_obj[0].title
    #
    #
    # def get_filters_title(self, obj):
    #     return obj.filters.title


class CatEventSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id','title','icon','file']


    def get_file(self, obj):
        resources = obj.category.all()
        interive_image = Interive.objects.filter(resource_interive__in=resources).first()
        if interive_image and interive_image.file:
            return interive_image.file.url
        return None



class CategorySerializer(serializers.ModelSerializer):
    category = ResourceAdminSerializer(many=True,read_only=True)
    class Meta:
        model = Category
        fields = ['id','title', 'icon', 'order', 'category']
    def get_category(self, obj):
        return obj.category.all()



