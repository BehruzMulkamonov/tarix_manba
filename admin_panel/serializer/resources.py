from itertools import zip_longest
from django.db import transaction
from django.core.files.base import ContentFile
from rest_framework import serializers
from rest_framework.request import Request

import json

from Config import settings
from resources.models import Category, PeriodFilter, Filters, Resource, Province, Interive, Attributes, Contents, \
    FilterCategories
import uuid

import base64
import six
import re



class Base64FileField(serializers.FileField):
    def to_internal_value(self, data):
        if isinstance(data, six.string_types):
            if 'data:' in data and ';base64,' in data:
                header, data = data.split(';base64,')

            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_file')

            file_name = str(uuid.uuid4())[:12]
            file_extension = self.get_file_extension(file_name, decoded_file)
            complete_file_name = f"{file_name}.{file_extension}"

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64FileField, self).to_internal_value(data)
    
    def get_file_extension(self, file_name, decoded_file):
        try:
            import magic
            file_mime_type = magic.from_buffer(decoded_file, mime=True)
            return file_mime_type.split('/')[-1]
        except ImportError:
            return 'jpg'


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
        fields = ('id', 'title', 'icon','image' ,'order', 'interactive', 'created_time', 'updated_time', 'categories',)
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
    file = Base64FileField(max_length=None, use_url=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Interive
        fields = ['resource_interive','status','status_display', 'title', 'file', 'link', 'latitude', 'longitude', 'created_time', 'updated_time']

    def create(self, validated_data):
        latitude = validated_data.pop('latitude', None)
        longitude = validated_data.pop('longitude', None)
        interive_instance = Interive.objects.create(**validated_data)
        if latitude:
            interive_instance.latitude = latitude
        if longitude:
            interive_instance.longitude = longitude
        interive_instance.save()
        return interive_instance

    def update(self, instance, validated_data):
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        return super().update(instance, validated_data)
    

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
    interive_list = serializers.SerializerMethodField(required=False, read_only=True)
    attributes_list = serializers.SerializerMethodField(required=False, read_only=True)
    contents_list = serializers.SerializerMethodField(required=False, read_only=True)
    cat_name = serializers.SerializerMethodField(required=False, read_only=True)
    filter_category_name = serializers.SerializerMethodField(required=False, read_only=True)
    filters_name = serializers.SerializerMethodField(required=False, read_only=True)
    period_filter_name = serializers.SerializerMethodField(required=False, read_only=True)
    image = Base64FileField(max_length=None, use_url=True)
    province_name = serializers.SerializerMethodField(required=False, read_only=True)
    contents_title_list = serializers.ListField(
        child=serializers.CharField(max_length=None, required=False),
        write_only=True,
        required=False
    )
    contents_description_list = serializers.ListField(
        child=serializers.CharField(max_length=None, required=False),
        write_only=True,
        required=False
    )
    attributes_title_list = serializers.ListField(
        child=serializers.CharField(max_length=None, required=False),
        write_only=True,
        required=False
    )
    attributes_description_list = serializers.ListField(
        child=serializers.CharField(max_length=None, required=False),
        write_only=True,
        required=False

    )

    interive_data_list = serializers.ListField(
        child=serializers.DictField(child=serializers.CharField(max_length=None, required=False)),
        write_only=True,
        required=False
    )

    # status_list = serializers.ListField(
    #     child=serializers.CharField(max_length=None, required=False),
    #     write_only=True,
    #     required=False
    # )
    # interive_title_list = serializers.ListField(
    #     child=serializers.CharField(max_length=None, required=False),
    #     write_only=True,
    #     required=False
    # )
    # interive_file_list = serializers.ListField(
    #     child=Base64FileField(max_length=1000, allow_empty_file=False, use_url=False),
    #     write_only=True,
    #     required=False
    # )
    # link_list = serializers.ListField(
    #     child=serializers.URLField(max_length=2000, allow_blank=True, required=False),
    #     write_only=True,
    #     required=False
    # )
    # latitude_list = serializers.ListField(
    #     child=serializers.FloatField(max_value=90, min_value=-90, required=False),
    #     write_only=True,
    #     required=False
    # )
    # longitude_list = serializers.ListField(
    #     child=serializers.FloatField(max_value=180, min_value=-180, required=False),
    #     write_only=True,
    #     required=False
    # )


    class Meta:
        model = Resource
        fields = (
            'id', 'category', 'filter_category', 'filters', 'period_filter', 'title', 'image', 'content', 'province_name','statehood',
            'province', 'interive', 'interive_data_list',
            'attributes_title_list', 'attributes_description_list', 'attributes',
            'contents_title_list', 'contents_description_list', 'contents',
            'interive_list', 'attributes_list', 'contents_list',
            'cat_name', 'filter_category_name', 'filters_name', 'period_filter_name',
            'created_time', 'updated_time'
        )

    def get_interive_list(self, obj):
        return InteriveAdminSerializer(obj.resource_interive.all(), many=True).data

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
    def get_province_name(self,obj):
        province = obj.province
        if province:
            return province.title

    @staticmethod
    def create_contents(resource, title_list, description_list):
        if title_list or description_list:
            for title, description in zip_longest(title_list or [''], description_list or [''], fillvalue=''):
                Contents.objects.create(resource_content=resource, contents_title=title, contents_description=description)
        else:
            Contents.objects.create(resource_content=resource, contents_title='', contents_description='')

    @staticmethod
    def create_attributes(resource, title_list, description_list):
        if title_list or description_list:
            for title, description in zip_longest(title_list or [''], description_list or [''], fillvalue=''):
                Attributes.objects.create(resource_attribute=resource, attributes_title=title, attributes_description=description)
        else:
            Attributes.objects.create(resource_attribute=resource, attributes_title='', attributes_description='')



    @staticmethod
    def create_interive(resource, interive_data_list):
        for interive_data in interive_data_list:
            Interive.objects.create(
                resource_interive=resource,
                status=interive_data.get('status', ''),
                title=interive_data.get('title', ''),
                file=interive_data.get('file', None),
                link=interive_data.get('link', ''),
                latitude=interive_data.get('latitude', None),
                longitude=interive_data.get('longitude', None)
            )

    # @staticmethod
    # def create_interive(resource, status_list, title_list, file_list, link_list, latitude_list, longitude_list):
    # # To'ldirish qiymatlarini o'rnatish
    #     status_list = status_list or ['']
    #     title_list = title_list or ['']
    #     file_list = file_list or [None]
    #     link_list = link_list or ['']
    #     latitude_list = latitude_list or [None]
    #     longitude_list = longitude_list or [None]

    #     # Har bir element uchun zip_longest yordamida ro'yxatlarni birlashtirish
    #     for status, title, file, link, latitude, longitude in zip_longest(
    #             status_list, title_list, file_list, link_list, latitude_list, longitude_list,
    #             fillvalue=''):
    #         Interive.objects.create(
    #             resource_interive=resource,
    #             status=status,
    #             title=title,
    #             file=file,
    #             link=link,
    #             latitude=latitude,
    #             longitude=longitude
    #         )

    

    @transaction.atomic
    def create(self, validated_data):
        contents_title_list = validated_data.pop('contents_title_list', [])
        contents_description_list = validated_data.pop('contents_description_list', [])
        attributes_title_list = validated_data.pop('attributes_title_list', [])
        attributes_description_list = validated_data.pop('attributes_description_list', [])
        # status_list = validated_data.pop('status_list', [])
        # interive_title_list = validated_data.pop('interive_title_list', [])
        # interive_file_list = validated_data.pop('interive_file_list', [])
        
        interive_data_list = validated_data.pop('interive_data_list', [])

        resource = Resource.objects.create(**validated_data)

        self.create_contents(resource, contents_title_list, contents_description_list)
        self.create_attributes(resource, attributes_title_list, attributes_description_list)
        self.create_interive(resource, interive_data_list)


        return resource

    # @staticmethod
    # def create_interive(resource, interive_data_list):
    #     for interive_data in interive_data_list:
    #         Interive.objects.create(
    #             resource_interive=resource,
    #             status=interive_data.get('status', ''),
    #             title=interive_data.get('title', ''),
    #             file=interive_data.get('file', None),
    #             link=interive_data.get('link', ''),
    #             latitude=interive_data.get('latitude', None),
    #             longitude=interive_data.get('longitude', None)
    #         )
    #     link_list = validated_data.pop('link_list', [])
    #     latitude_list = validated_data.pop('latitude_list', [])
    #     longitude_list = validated_data.pop('longitude_list', [])

    #     resource = Resource.objects.create(**validated_data)

    #     self.create_contents(resource, contents_title_list, contents_description_list)
    #     self.create_attributes(resource, attributes_title_list, attributes_description_list)
    #     self.create_interive(resource, status_list, interive_title_list, interive_file_list, link_list, latitude_list, longitude_list)

    #     return resource

    @transaction.atomic
    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category)
        instance.filter_category = validated_data.get('filter_category', instance)
        instance.filter_category = validated_data.get('filter_category', instance.filter_category)
        instance.filters = validated_data.get('filters', instance.filters)
        instance.period_filter = validated_data.get('period_filter', instance.period_filter)
        instance.title = validated_data.get('title', instance.title)
        instance.image = validated_data.get('image', instance.image)
        instance.content = validated_data.get('content', instance.content)
        instance.statehood = validated_data.get('statehood', instance.statehood)
        instance.province = validated_data.get('province', instance.province)
        instance.save()

        contents_title_list = validated_data.pop('contents_title_list', [])
        contents_description_list = validated_data.pop('contents_description_list', [])
        attributes_title_list = validated_data.pop('attributes_title_list', [])
        attributes_description_list = validated_data.pop('attributes_description_list', [])
        interive_data_list = validated_data.pop('interive_data_list', [])
        # status_list = validated_data.pop('status_list', [])
        # interive_title_list = validated_data.pop('interive_title_list', [])
        # interive_file_list = validated_data.pop('interive_file_list', [])
        # link_list = validated_data.pop('link_list', [])
        # latitude_list = validated_data.pop('latitude_list', [])
        # longitude_list = validated_data.pop('longitude_list', [])

        instance.resource_content.all().delete()
        instance.resource_attribute.all().delete()
        instance.resource_interive.all().delete()

        self.create_contents(instance, contents_title_list, contents_description_list)
        self.create_attributes(instance, attributes_title_list, attributes_description_list)
        self.create_interive(instance, interive_data_list)

        return instance

