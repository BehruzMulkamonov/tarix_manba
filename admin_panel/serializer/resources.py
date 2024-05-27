from rest_framework import serializers
from rest_framework.request import Request

import json

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
        fields = ['resource_interive','status', 'title', 'file', 'link', 'latitude', 'longitude', 'created_time', 'updated_time']


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
    # interive_list = serializers.SerializerMethodField(required=False, read_only=True)
    # attributes_list = serializers.SerializerMethodField(required=False, read_only=True)
    # contents_list = serializers.SerializerMethodField(required=False, read_only=True)
    # cat_name = serializers.SerializerMethodField(required=False, read_only=True)
    # filter_category_name = serializers.SerializerMethodField(required=False, read_only=True)
    # filters_name = serializers.SerializerMethodField(required=False, read_only=True)
    # period_filter_name = serializers.SerializerMethodField(required=False, read_only=True)
    # contents_title_list = serializers.ListField(
    #     child=serializers.CharField(max_length=None,required=False),
    #     write_only=True,
    #     required=False
    #
    # )
    # contents_description_list = serializers.ListField(
    #     child=serializers.CharField(max_length=None,required=False),
    #     write_only=True,
    #     required=False
    #
    # )
    # attributes_title_list = serializers.ListField(
    #     child=serializers.CharField(max_length=None,required=False),
    #     write_only=True,
    #     required=False
    #
    # )
    # attributes_description_list = serializers.ListField(
    #     child=serializers.CharField(max_length=None,required=False),
    #     write_only=True,
    #     required=False
    #
    # )
    # status_list = serializers.ListField(
    #     child=serializers.CharField(max_length=None,required=False),
    #     write_only=True,
    #     required=False
    # )
    # interive_title_list = serializers.ListField(
    #     child=serializers.CharField(max_length=None,required=False),
    #     write_only=True,
    #     required=False
    # )
    #
    # interive_file_list = serializers.ListField(
    #     child=serializers.ImageField(max_length=1000, allow_empty_file=False, use_url=False),
    #     write_only=True,
    #     required=False
    # )
    # link_list = serializers.ListField(
    #     child=serializers.URLField(max_length=2000, allow_blank=True,required=False),
    #     write_only=True,
    #     required=False
    # )
    # latitude_list = serializers.ListField(
    #     child=serializers.FloatField(max_value=90, min_value=-90,required=False),
    #     write_only=True,
    #     required=False
    # )
    # longitude_list = serializers.ListField(
    #     child=serializers.FloatField(max_value=180, min_value=-180,required=False),
    #     write_only=True,
    #     required=False
    # )
    #


    class Meta:
        model = Resource
        fields = (
            'id', 'category', 'filter_category', 'filters', 'period_filter', 'title', 'image', 'content', 'statehood',
            # 'province','interive','status_list','interive_title_list',
            # 'interive_file_list','link_list','latitude_list','longitude_list',
            # 'attributes_title_list', 'attributes_description_list','attributes',
            # 'contents_title_list', 'contents_description_list','contents',
            # 'interive_list','attributes_list','contents_list',
            # 'cat_name','filter_category_name','filters_name','period_filter_name',
            'created_time', 'updated_time')


<<<<<<< HEAD
    # def get_interive_list(self, obj):
    #     return InteriveAdminSerializer(obj.resource_interives.all(), many=True).data
    #
    # def get_attributes_list(self, obj):
    #     return AttributesAdminSerializer(obj.resource_attribute.all(), many=True).data
    # def get_contents_list(self, obj):
    #     return ContentsAdminSerializer(obj.resource_content.all(), many=True).data
    #
    # def get_cat_name(self, obj):
    #     cat = obj.category
    #     if cat:
    #         return cat.title
    #
    # def get_filter_category_name(self, obj):
    #     title = obj.filter_category
    #     if title:
    #         return title.title
    #
    # def get_filters_name(self, obj):
    #     filters = obj.filters
    #     if filters:
    #         return filters.title
    #
    # def get_period_filter_name(self, obj):
    #     period = obj.period_filter
    #     if period:
    #         return period.title
    #
    # # def create(self, validated_data):
    #     contents_title_list = validated_data.pop('contents_title_list', [])
    #     contents_description_list = validated_data.pop('contents_description_list', [])
    #     attributes_title_list = validated_data.pop('attributes_title_list', [])
    #     attributes_description_list = validated_data.pop('attributes_description_list', [])
    #     status_list = validated_data.pop('status_list', [])
    #     interive_title_list = validated_data.pop('interive_title_list', [])
    #     interive_file_list = validated_data.pop('interive_file_list', [])
    #     link_list = validated_data.pop('link_list', [])
    #     latitude_list = validated_data.pop('latitude_list', [])
    #     longitude_list = validated_data.pop('longitude_list', [])
    #
    #
    #     resource = Resource.objects.create(**validated_data)
    #     for contents_title in contents_title_list:
    #         for contents_description in contents_description_list:
    #             Contents.objects.create(resource_content=resource, contents_title=contents_title, contents_description=contents_description)
    #
    #     for attributes_title in attributes_title_list:
    #         for attributes_description in attributes_description_list:
    #             Attributes.objects.create(resource_attribute=resource, attributes_title=attributes_title, attributes_description=attributes_description)
    #
    #     for status,title,file,link,latitude,longitude in zip(status_list,interive_title_list,interive_file_list,link_list,latitude_list,longitude_list):
    #         Interive.objects.create(resource_interive=resource,status=status,title=title,file=file,link=link,latitude=latitude,longitude=longitude)
    #
    #
    #
    #
    #     return resource
=======
    def get_interive_list(self, obj):
        return InteriveAdminSerializer(obj.resource_interives.all(), many=True).data

    def get_attributes_list(self, obj):
        return AttributesAdminSerializer(obj.resource_attribute.all(), many=True).data
    def get_contents_list(self, obj):
        return ContentsAdminSerializer(obj.resource_content.all(), many=True).data

    def get_cat_name(self, obj):
        cat = obj.category
        if cat:
            return cat.title

    def get_filter_category_name(self, obj):
        title = obj.filter_category
        if title:
            return title.title

    def get_filters_name(self, obj):
        filters = obj.filters
        if filters:
            return filters.title

    def get_period_filter_name(self, obj):
        period = obj.period_filter
        if period:
            return period.title

    def create(self, validated_data):
        contents_title_list = validated_data.pop('contents_title_list', [])
        contents_description_list = validated_data.pop('contents_description_list', [])
        attributes_title_list = validated_data.pop('attributes_title_list', [])
        attributes_description_list = validated_data.pop('attributes_description_list', [])
        status_list = validated_data.pop('status_list', [])
        interive_title_list = validated_data.pop('interive_title_list', [])
        interive_file_list = validated_data.pop('interive_file_list', [])
        link_list = validated_data.pop('link_list', [])
        latitude_list = validated_data.pop('latitude_list', [])
        longitude_list = validated_data.pop('longitude_list', [])


        resource = Resource.objects.create(**validated_data)
        con_title_list = json.loads(contents_title_list)
        con_description_list = json.loads(contents_description_list)
        for conetnts_title in con_title_list:
            for contents_description in con_description_list:
                Contents.objects.create(resource_content=resource, contents_title=conetnts_title, contents_description=contents_description)

        att_title_list = json.loads(attributes_title_list)
        att_description_list = json.loads(attributes_description_list)

        for attributes_title in att_title_list:
            for attributes_description in att_description_list:
                Attributes.objects.create(resource_attribute=resource, attributes_title=attributes_title, attributes_description=attributes_description)

        stat_list = json.loads(status_list)
        inter_title_list = json.loads(interive_title_list)
        inter_file_list = json.loads(interive_file_list)
        links_list = json.loads(link_list)
        latit_list = json.loads(latitude_list)
        long_list = json.loads(longitude_list)
        for status,title,file,link,latitude,longitude in zip(stat_list,inter_title_list,inter_file_list,links_list,latit_list,long_list):
            Interive.objects.create(resource_interive=resource,status=status,title=title,file=file,link=link,latitude=latitude,longitude=longitude)




        return resource
>>>>>>> 4f31b2bdb70b23a0caa4ea9850b62fcbcf7ac032
