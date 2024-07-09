from itertools import zip_longest
from django.db import transaction
from django.core.files.base import ContentFile
from rest_framework import serializers
from rest_framework.request import Request
import json
from Config import settings
from resources.models import Category, PeriodFilter, Filters, Resource, Province,  Attributes, Contents, \
    FilterCategories, Gallery, File, Audio, Virtual_reality, Video, Location
import uuid
import base64
import six
import re
import logging

logger = logging.getLogger(__name__)

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

# class Base64FileField(serializers.FileField):
#     def to_internal_value(self, data):
#         # If data is a base64 string, handle it here.
#         if isinstance(data, str) and data.startswith('data:'):
#             # Get the file format and base64 string
#             format, imgstr = data.split(';base64,') 

#             # Handle incorrect padding
#             imgstr += '=' * (4 - len(imgstr) % 4)
            
#             try:
#                 # Decode the base64 string
#                 decoded_file = base64.b64decode(imgstr)
#             except (TypeError, binascii.Error):
#                 raise serializers.ValidationError("Invalid image format")

#             # Generate file name
#             file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
#             # Get the file extension from the format part
#             file_extension = format.split('/')[-1]
            
#             complete_file_name = f"{file_name}.{file_extension}"
            
#             data = ContentFile(decoded_file, name=complete_file_name)

#         return super(Base64FileField, self).to_internal_value(data)



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


# class InteriveAdminSerializer(serializers.ModelSerializer):
#     file = Base64FileField(max_length=None, use_url=True, allow_null=True)
#     status_display = serializers.CharField(source='get_status_display', read_only=True)

#     class Meta:
#         model = Interive
#         fields = ['status', 'status_display', 'title', 'file', 'link', 'latitude', 'longitude', 'created_time', 'updated_time']
#         extra_kwargs = {
#             'file': {'required': False, 'allow_null': True},
#         }

#         def validate_file(self, value):
#         # Allowing null values for the file field
#             if value is None:
#                 return None
#             return value

#     def create(self, validated_data):
#         latitude = validated_data.pop('latitude', None)
#         longitude = validated_data.pop('longitude', None)
#         interive_instance = Interive.objects.create(**validated_data)
#         if latitude:
#             interive_instance.latitude = latitude
#         if longitude:
#             interive_instance.longitude = longitude
#         interive_instance.save()
#         return interive_instance

#     def update(self, instance, validated_data):
#         instance.latitude = validated_data.get('latitude', instance.latitude)
#         instance.longitude = validated_data.get('longitude', instance.longitude)
#         return super().update(instance, validated_data)
    


class AttributesAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attributes
        fields = ['resource_attribute', 'attributes_title', 'attributes_description', 'created_time', 'updated_time']


class ContentsAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contents
        fields = ['resource_content', 'contents_title', 'contents_description', 'created_time', 'updated_time']

class GallerySerializer(serializers.ModelSerializer):
    image = Base64FileField(max_length=None, use_url=True, allow_null=True)

    class Meta:
        model = Gallery
        fields = ['id', 'resource_gallery', 'title', 'image', 'created_time', 'updated_time']

class FileSerializer(serializers.ModelSerializer):
    file = Base64FileField(max_length=None, use_url=True, allow_null=True)

    class Meta:
        model = File
        fields = ['id', 'resource_file', 'title', 'file', 'created_time', 'updated_time']

class AudioSerializer(serializers.ModelSerializer):
    file = Base64FileField(max_length=None, use_url=True, allow_null=True)

    class Meta:
        model = Audio
        fields = ['id', 'resource_audio', 'title', 'file', 'created_time', 'updated_time']

class VirtualRealitySerializer(serializers.ModelSerializer):
    file = Base64FileField(max_length=None, use_url=True, allow_null=True)

    class Meta:
        model = Virtual_reality
        fields = ['id', 'resource_virtual_reality', 'title', 'file', 'created_time', 'updated_time']

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'resource_video', 'title', 'link', 'created_time', 'updated_time']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'resource_location', 'title', 'latitude', 'longitude', 'created_time', 'updated_time']

class ResourceAdminSerializer(serializers.ModelSerializer):
    # interative = InteriveAdminSerializer(many=False, read_only=True)
    attributes = AttributesAdminSerializer(many=True, read_only=True)
    contents = ContentsAdminSerializer(many=True, read_only=True)

    galleries = GallerySerializer(many=True, read_only=True)
    files = FileSerializer(many=True, read_only=True)
    audios = AudioSerializer(many=True, read_only=True)
    virtual_realities = VirtualRealitySerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)
    locations = LocationSerializer(many=True, read_only=True)

    # interive_list = serializers.SerializerMethodField(required=False, read_only=True)
    attributes_list = serializers.SerializerMethodField(required=False, read_only=True)
    contents_list = serializers.SerializerMethodField(required=False, read_only=True)
    # interive list 
    galleries_list = serializers.SerializerMethodField(required=False, read_only=True)
    files_list = serializers.SerializerMethodField(required=False, read_only=True)
    audios_list = serializers.SerializerMethodField(required=False, read_only=True)
    virtual_realities_list = serializers.SerializerMethodField(required=False, read_only=True)
    videos_list = serializers.SerializerMethodField(required=False, read_only=True)
    locations_list = serializers.SerializerMethodField(required=False, read_only=True)
    # 
    cat_name = serializers.SerializerMethodField(required=False, read_only=True)
    filter_category_name = serializers.SerializerMethodField(required=False, read_only=True)
    filters_name = serializers.SerializerMethodField(required=False, read_only=True)
    period_filter_name = serializers.SerializerMethodField(required=False, read_only=True)
    image = Base64FileField(max_length=None, use_url=True, allow_null=True)
    province_name = serializers.SerializerMethodField(required=False, read_only=True)

    galleries_title_list = serializers.ListField(child=serializers.CharField(max_length=None, required=False), write_only=True, required=False)
    galleries_image_list = serializers.ListField(child=Base64FileField(max_length=None, use_url=True, required=False), write_only=True, required=False)

    files_title_list = serializers.ListField(child=serializers.CharField(max_length=None, required=False), write_only=True, required=False)
    files_file_list = serializers.ListField(child=Base64FileField(max_length=None, use_url=True, required=False), write_only=True, required=False)

    audios_title_list = serializers.ListField(child=serializers.CharField(max_length=None, required=False), write_only=True, required=False)
    audios_file_list = serializers.ListField(child=Base64FileField(max_length=None, use_url=True, required=False), write_only=True, required=False)

    virtual_realities_title_list = serializers.ListField(child=serializers.CharField(max_length=None, required=False), write_only=True, required=False)
    virtual_realities_file_list = serializers.ListField(child=Base64FileField(max_length=None, use_url=True, required=False), write_only=True, required=False)

    videos_title_list = serializers.ListField(child=serializers.CharField(max_length=None, required=False), write_only=True, required=False)
    videos_link_list = serializers.ListField(child=serializers.URLField(required=False), write_only=True, required=False)

    locations_title_list = serializers.ListField(child=serializers.CharField(max_length=None, required=False), write_only=True, required=False)
    locations_latitude_list = serializers.ListField(child=serializers.CharField(max_length=None, required=False), write_only=True, required=False)
    locations_longitude_list = serializers.ListField(child=serializers.CharField(max_length=None, required=False), write_only=True, required=False)

    contents_title_list = serializers.ListField(child=serializers.CharField(max_length=None, required=False), write_only=True, required=False)
    contents_description_list = serializers.ListField(child=serializers.CharField(max_length=None, required=False), write_only=True, required=False)
    attributes_title_list = serializers.ListField(child=serializers.CharField(max_length=None, required=False), write_only=True, required=False)
    attributes_description_list = serializers.ListField(child=serializers.CharField(max_length=None, required=False), write_only=True, required=False)
    # interive_data_list = serializers.ListField(child=serializers.DictField(child=serializers.CharField(max_length=None, required=False)), write_only=True, required=False)
    filter_list = serializers.ListField(child=serializers.IntegerField(), write_only=True, required=False)

    class Meta:
        model = Resource
        fields = (
            'id', 'category', 'filter_category', 'period_filter', 'title', 'image', 'content', 'province_name', 'statehood',
            'province',   'attributes_title_list', 'attributes_description_list', 'attributes', 'galleries_title_list', 'galleries_image_list',
            'contents_title_list', 'contents_description_list', 'contents', 'galleries', 'files', 'audios', 'virtual_realities', 'videos',
            'locations',  'attributes_list', 'contents_list', 'galleries_list', 'files_list', 'audios_list', 'virtual_realities_list', 
            'videos_list', 'locations_list','cat_name', 'filter_category_name', 'filters_name', 'period_filter_name', 
            'filter_list', 'created_time', 'updated_time', 'files_title_list', 'files_file_list', 'audios_title_list', 
            'audios_file_list', 'virtual_realities_title_list', 'virtual_realities_file_list', 'videos_title_list', 
            'videos_link_list', 'locations_title_list', 'locations_latitude_list', 'locations_longitude_list'
        )

    # def get_interive_list(self, obj):
    #     return InteriveAdminSerializer(obj.interative, many=False).data

    def get_attributes_list(self, obj):
        return AttributesAdminSerializer(obj.resource_attribute.all(), many=True).data

    def get_contents_list(self, obj):
        return ContentsAdminSerializer(obj.resource_content.all(), many=True).data

    def get_galleries_list(self, obj):
        return GallerySerializer(obj.resource_gallery.all(), many=True).data

    def get_files_list(self, obj):
        return FileSerializer(obj.resource_file.all(), many=True).data

    def get_audios_list(self, obj):
        return AudioSerializer(obj.resource_audio.all(), many=True).data

    def get_virtual_realities_list(self, obj):
        return VirtualRealitySerializer(obj.resource_virtual_reality.all(), many=True).data

    def get_videos_list(self, obj):
        return VideoSerializer(obj.resource_video.all(), many=True).data

    def get_locations_list(self, obj):
        return LocationSerializer(obj.resource_location.all(), many=True).data

    def get_cat_name(self, obj):
        cat = obj.category
        if cat:
            return cat.title

    def get_filter_category_name(self, obj):
        title = obj.filter_category
        if title:
            return title.title

    def get_filters_name(self, obj):
        filters = obj.filters.all()
        if filters:
            return [filter.id for filter in filters]
        return []

    def get_period_filter_name(self, obj):
        period = obj.period_filter
        if period:
            return period.title

    def get_province_name(self, obj):
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

    # @staticmethod
    # def create_galleries(resource, galleries_data):
    #     for gallery_data in galleries_data:
    #         Gallery.objects.create(resource_gallery=resource, **gallery_data)
    @staticmethod
    def create_galleries(resource, title_list, image_list):
        if title_list or image_list:
            for title, image in zip_longest(title_list or [''], image_list or [''], fillvalue=''):
                Gallery.objects.create(resource_gallery=resource, title=title, image=image)
        else:
            Gallery.objects.create(resource_gallery=resource, title='', image=None)

    # @staticmethod
    # def create_files(resource, files_data):
    #     for file_data in files_data:
    #         File.objects.create(resource_file=resource, **file_data)

    # @staticmethod
    # def create_audios(resource, audios_data):
    #     for audio_data in audios_data:
    #         Audio.objects.create(resource_audio=resource, **audio_data)

    # @staticmethod
    # def create_virtual_realities(resource, virtual_realities_data):
    #     for virtual_reality_data in virtual_realities_data:
    #         Virtual_reality.objects.create(resource_virtual_reality=resource, **virtual_reality_data)

    # @staticmethod
    # def create_videos(resource, videos_data):
    #     for video_data in videos_data:
    #         Video.objects.create(resource_video=resource, **video_data)
    @staticmethod
    def create_files(resource, title_list, file_list):
        if title_list or file_list:
            for title, file in zip_longest(title_list or [''], file_list or [''], fillvalue=''):
                File.objects.create(resource_file=resource, title=title, file=file)
        else:
            File.objects.create(resource_file=resource, title='', file=None)

    @staticmethod
    def create_audios(resource, title_list, file_list):
        if title_list or file_list:
            for title, file in zip_longest(title_list or [''], file_list or [''], fillvalue=''):
                Audio.objects.create(resource_audio=resource, title=title, file=file)
        else:
            Audio.objects.create(resource_audio=resource, title='', file=None)

    @staticmethod
    def create_virtual_realities(resource, title_list, file_list):
        if title_list or file_list:
            for title, file in zip_longest(title_list or [''], file_list or [''], fillvalue=''):
                Virtual_reality.objects.create(resource_virtual_reality=resource, title=title, file=file)
        else:
            Virtual_reality.objects.create(resource_virtual_reality=resource, title='', file=None)

    @staticmethod
    def create_videos(resource, title_list, link_list):
        if title_list or link_list:
            for title, link in zip_longest(title_list or [''], link_list or [''], fillvalue=''):
                Video.objects.create(resource_video=resource, title=title, link=link)
        else:
            Video.objects.create(resource_video=resource, title='', link=None)

    # @staticmethod
    # def create_locations(resource, locations_data):
    #     for location_data in locations_data:
    #         Location.objects.create(resource_location=resource, **location_data)

    @staticmethod
    def create_locations(resource, title_list, latitude_list, longitude_list):
        if title_list or latitude_list or longitude_list:
            for title, latitude, longitude in zip_longest(title_list or [''], latitude_list or [''], longitude_list or [''], fillvalue=''):
                Location.objects.create(resource_location=resource, title=title, latitude=latitude, longitude=longitude)
        else:
            Location.objects.create(resource_location=resource, title='', latitude='', longitude='')

    @transaction.atomic
    def create(self, validated_data):
        contents_title_list = validated_data.pop('contents_title_list', [])
        contents_description_list = validated_data.pop('contents_description_list', [])
        attributes_title_list = validated_data.pop('attributes_title_list', [])
        attributes_description_list = validated_data.pop('attributes_description_list', [])
        # interive_data_list = validated_data.pop('interive_data_list', [])
        galleries_title_list = validated_data.pop('galleries_title_list', [])
        galleries_image_list = validated_data.pop('galleries_image_list', [])
        files_title_list = validated_data.pop('files_title_list', [])
        files_file_list = validated_data.pop('files_file_list', [])
        audios_title_list = validated_data.pop('audios_title_list', [])
        audios_file_list = validated_data.pop('audios_file_list', [])
        virtual_realities_title_list = validated_data.pop('virtual_realities_title_list', [])
        virtual_realities_file_list = validated_data.pop('virtual_realities_file_list', [])
        videos_title_list = validated_data.pop('videos_title_list', [])
        videos_link_list = validated_data.pop('videos_link_list', [])
        locations_title_list = validated_data.pop('locations_title_list', [])
        locations_latitude_list = validated_data.pop('locations_latitude_list', [])
        locations_longitude_list = validated_data.pop('locations_longitude_list', [])
        galleries_data = validated_data.pop('galleries', [])

        files_data = validated_data.pop('files', [])
        audios_data = validated_data.pop('audios', [])
        virtual_realities_data = validated_data.pop('virtual_realities', [])
        videos_data = validated_data.pop('videos', [])
        locations_data = validated_data.pop('locations', [])
        filter_list = validated_data.pop('filter_list', [])

        resource = Resource.objects.create(**validated_data)

        self.create_contents(resource, contents_title_list, contents_description_list)
        self.create_attributes(resource, attributes_title_list, attributes_description_list)
        # self.create_interive(resource, interive_data_list)
        # self.create_galleries(resource, galleries_data)
        self.create_galleries(resource, galleries_title_list, galleries_image_list)
        self.create_files(resource, files_title_list, files_file_list)
        self.create_audios(resource, audios_title_list, audios_file_list)
        self.create_virtual_realities(resource, virtual_realities_title_list, virtual_realities_file_list)
        self.create_videos(resource, videos_title_list, videos_link_list)
        self.create_locations(resource, locations_title_list, locations_latitude_list, locations_longitude_list)
        
        resource.filters.set(filter_list)

        return resource

    @transaction.atomic
    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category)
        instance.filter_category = validated_data.get('filter_category', instance.filter_category)
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
        # interive_data_list = validated_data.pop('interive_data_list', [])
        filter_list = validated_data.pop('filter_list', [])

        instance.resource_content.all().delete()
        instance.resource_attribute.all().delete()
        # instance.interative.delete()

        self.create_contents(instance, contents_title_list, contents_description_list)
        self.create_attributes(instance, attributes_title_list, attributes_description_list)
        # self.create_interive(instance, interive_data_list)

        instance.filters.set(filter_list)

        return instance
