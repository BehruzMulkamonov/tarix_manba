from rest_framework import serializers

from resources.models import Category, PeriodFilter, Filters, Resource, Province, Interive, Attributes, Contents


class CategoryAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'icon', 'order', 'interactive','created_time','updated_time')



class PeriodFilterAdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeriodFilter
        fields = ('id', 'title','created_time','updated_time' )



class FilterCategoriesAdminSerializer(serializers.ModelSerializer):
    category = CategoryAdminSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'title',  'category','created_time','updated_time')


class FiltersAdminSerializer(serializers.ModelSerializer):
    filter_category = FilterCategoriesAdminSerializer(many=True, read_only=True)


    class Meta:
        model = Filters
        fields = ('id', 'title','filter_category','created_time','updated_time')


class ProvinceAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ('id', 'title','created_time','updated_time')


class InteriveAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interive
        fields = ['status', 'title', 'file', 'link', 'latitude', 'longitude','created_time','updated_time']

class AttributesAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attributes
        fields = ['resource_attribute', 'attributes_title', 'attributes_description','created_time','updated_time']


class ContentsAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contents
        fields = ['resource_content', 'contents_title', 'contents_description','created_time','updated_time']


class ResourceAdminSerializer(serializers.ModelSerializer):
    interive = InteriveAdminSerializer(many=True)
    attributes = AttributesAdminSerializer(many=True)
    contents = ContentsAdminSerializer(many=True)

    class Meta:
        model = Resource
        fields = (
        'id', 'category', 'filter_category', 'filters', 'period_filter', 'title', 'image', 'content', 'statehood',
        'province', 'interive', 'attributes', 'contents','created_time','updated_time')

    def create(self, validated_data):
        interive_data = validated_data.pop('interive')
        attributes_data = validated_data.pop('attributes')
        contents_data = validated_data.pop('contents')

        resource = Resource.objects.create(**validated_data)

        for interive_item in interive_data:
            Interive.objects.create(resource_content=resource, **interive_item)

        for attributes_item in attributes_data:
            Attributes.objects.create(resource_attribute=resource, **attributes_item)

        for contents_item in contents_data:
            Contents.objects.create(resource_content=resource, **contents_item)

        return resource