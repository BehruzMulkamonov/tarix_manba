from rest_framework import serializers
from rest_framework.request import Request

from Config import settings
from resources.models import Category, PeriodFilter, Filters, Resource, Province, Interive, Attributes, Contents, \
    FilterCategories


class FiltersAdminSerializer(serializers.ModelSerializer):
    filter_categories_name = serializers.SerializerMethodField()
    filter_cat_id = serializers.SerializerMethodField()
    cat_id = serializers.SerializerMethodField()
    cat_title = serializers.SerializerMethodField()

    class Meta:
        model = Filters
        fields = ('id', 'title', 'filter_category', 'created_time',
                  'updated_time', 'filter_cat_id', 'filter_categories_name', 'cat_id',
                  'cat_title',)

    def get_filter_categories_name(self, obj):
        filter_cat = obj.filter_category
        if filter_cat:
            return filter_cat.title

    def get_filter_cat_id(self, obj):
        filter_cat = obj.filter_category
        if filter_cat:
            return filter_cat.id

    def get_cat_id(self, obj):
        cat_id = obj.filter_category
        if cat_id:
            cat = cat_id.category
            if cat:
                return cat.id

    def get_cat_title(self, obj):
        cat_name = obj.filter_category
        if cat_name:
            cat = cat_name.category
            if cat:
                return cat.title


class FilterCategoriesAdminSerializer(serializers.ModelSerializer):
    filters_category = FiltersAdminSerializer(many=True, read_only=True)
    cat_title = serializers.SerializerMethodField()
    cat_id = serializers.SerializerMethodField()

    class Meta:
        model = FilterCategories
        fields = ('id', 'title', 'category', 'created_time', 'updated_time', 'filters_category', 'cat_title', 'cat_id')
        extra_kwargs = {
            'filters_category': {'read_only': True, 'required': False},
        }

    def get_filters_category(self, obj):
        return obj.filters_category.all()

    def get_cat_title(self, obj):
        title = obj.category
        if title:
            return title.title

    def get_cat_id(self, obj):
        cat = obj.category
        if cat:
            return cat.id


class CategoryAdminSerializer(serializers.ModelSerializer):
    categories = FilterCategoriesAdminSerializer(many=True, read_only=True)



    class Meta:
        model = Category
        fields = ('id', 'title', 'icon', 'order', 'interactive', 'created_time', 'updated_time', 'categories',)
        extra_kwargs = {
            'categories': {'read_only': True, 'required': False},
        }



    def get_categories(self, obj):
        return obj.categories.all()








class PeriodFilterAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodFilter
        fields = ('id', 'title', 'created_time', 'updated_time')


class ProvinceAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ('id', 'title','latitude', 'longitude', 'created_time', 'updated_time')


class InteriveAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interive
        fields = ['status', 'title', 'file', 'link', 'latitude', 'longitude', 'created_time', 'updated_time']


class AttributesAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attributes
        fields = ['resource_attribute', 'attributes_title', 'attributes_description', 'created_time', 'updated_time']


class ContentsAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contents
        fields = ['resource_content', 'contents_title', 'contents_description', 'created_time', 'updated_time']

class ResourceAdminSerializer(serializers.ModelSerializer):
    interive = InteriveAdminSerializer(many=True, read_only=True)
    attributes = AttributesAdminSerializer(many=True, read_only=True)
    contents = ContentsAdminSerializer(many=True, read_only=True)
    contents_title_list = serializers.ListField(
        child=serializers.CharField(max_length=None),
        write_only=True
    )
    contents_description_list = serializers.ListField(
        child=serializers.CharField(max_length=None),
        write_only=True
    )

    class Meta:
        model = Resource
        fields = (
            'id', 'category', 'filter_category', 'filters', 'period_filter', 'title', 'image', 'content', 'statehood',
            'province', 'contents_title_list', 'contents_description_list','contents', 'created_time', 'updated_time')

    def create(self, validated_data):
        contents_title_list = validated_data.pop('contents_title_list', [])
        contents_description_list = validated_data.pop('contents_description_list', [])

        resource = Resource.objects.create(**validated_data)

        # Iterate over the lists and create Contents objects for each pair of title and description
        for title, description in zip(contents_title_list, contents_description_list):
            Contents.objects.create(resource_content=resource, contents_title=title, contents_description=description)

        return resource
