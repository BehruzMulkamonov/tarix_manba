from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from resources.models import Category, PeriodFilter, FilterCategories, Filters, Province, Resource
from resources.serializer import CategorySerializer, PeriodFilterSerializer, FilterCategoriesSerializer, \
    FiltersSerializer, ProvinceSerializer, ResourceSerializer


@api_view(['GET'])
def categoryListView(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    cats = Category.objects.all()

    result_page = paginator.paginate_queryset(cats, request)
    serializer = CategorySerializer(result_page, many=True)

    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def categoryDetailView(request, pk):
    cat = Category.objects.get(pk=pk)
    serializer = CategorySerializer(cat, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def periodFilterListView(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    period_filter = PeriodFilter.objects.all()
    result_page = paginator.paginate_queryset(period_filter, request)
    serializer = PeriodFilterSerializer(result_page, many=True)

    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def periodFilterDetailView(request, pk):
    period_filter = PeriodFilter.objects.get(pk=pk)
    serializer = PeriodFilterSerializer(period_filter, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def filterCategoriesListView(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10

    filter_categories = FilterCategories.objects.all()
    result_page = paginator.paginate_queryset(filter_categories, request)

    serializer = FilterCategoriesSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def filterCategoriesDetailView(request, pk):
    filter_categories = FilterCategories.objects.get(pk=pk)
    serializer = FilterCategoriesSerializer(filter_categories, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def filtersListView(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10

    filters = Filters.objects.all()
    result_page = paginator.paginate_queryset(filters, request)

    serializer = FiltersSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def filtersDetailView(request, pk):
    filters = Filters.objects.get(pk=pk)
    serializer = FiltersSerializer(filters, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def provinceListView(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    provinces = Province.objects.all()
    result_page = paginator.paginate_queryset(provinces, request)
    serializer = ProvinceSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def provinceDetailView(request, pk):
    province = Province.objects.get(pk=pk)
    serializer = ProvinceSerializer(province, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def resourceListView(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    resources = Resource.objects.all()
    result_page = paginator.paginate_queryset(resources, request)
    serializer = ResourceSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def resourceDetailView(request, pk):
    resource = Resource.objects.get(pk=pk)
    serializer = ResourceSerializer(resource, many=False)
    return Response(serializer.data)
