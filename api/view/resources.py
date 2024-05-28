from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from resources.models import Category, PeriodFilter, FilterCategories, Filters, Province, Resource
from resources.serializer import CategorySerializer, PeriodFilterSerializer, FilterCategoriesSerializer, \
    FiltersSerializer, ProvinceSerializer, ResourceSerializer, CatEventSerializer


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


@api_view(['GET'])
def catEventListView(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    resources = Category.objects.all()
    result_page = paginator.paginate_queryset(resources, request)
    serializer = CatEventSerializer(result_page, many=True)
    serialized_data = serializer.data

    for data in serialized_data:
        if data.get('file'):
            data['file'] = request.build_absolute_uri(data['file'])

    return paginator.get_paginated_response(serialized_data)


@api_view(['GET'])
def cateventDetailView(request, pk):
    resource = Category.objects.get(pk=pk)
    serializer = CatEventSerializer(resource, many=False)
    serialized_data = serializer.data

    # Check if 'file' key exists in the dictionary
    if 'file' in serialized_data:
        serialized_data['file'] = request.build_absolute_uri(serialized_data['file'])

    return Response(serialized_data)
