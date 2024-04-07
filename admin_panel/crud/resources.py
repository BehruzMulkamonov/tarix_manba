from rest_framework.decorators import api_view
from rest_framework.response import Response

from admin_panel.serializer.resources import CategoryAdminSerializer, PeriodFilterAdminSerializer, \
    FilterCategoriesAdminSerializer, FiltersAdminSerializer, ProvinceAdminSerializer, ResourceAdminSerializer
from resources.models import Category, PeriodFilter, FilterCategories, Filters, Province, Resource


@api_view(['GET'])
def categoryList(request):
    cats = Category.objects.all()
    serializer = CategoryAdminSerializer(cats, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def categoryDetail(request, pk):
    cat = Category.objects.get(pk=pk)
    serializer = CategoryAdminSerializer(cat, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createCategory(request):
    serializer = CategoryAdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def updateCategory(request, pk):
    try:
        cat = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=404)

    serializer = CategoryAdminSerializer(cat, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deleteCategory(request, pk):
    try:
        cat = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=404)

    cat.delete()
    return Response(status=204)

@api_view(['GET'])
def periodFilterList(request):
    periodfilter = PeriodFilter.objects.all()
    serializer = PeriodFilterAdminSerializer(periodfilter, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def periodFilterDetail(request, pk):
    periodfilter = PeriodFilter.objects.get(pk=pk)
    serializer = PeriodFilterAdminSerializer(periodfilter, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createPeriodFilter(request):
    serializer = PeriodFilterAdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def updatePeriodFilter(request, pk):
    try:
        periodfilter = PeriodFilter.objects.get(pk=pk)
    except PeriodFilter.DoesNotExist:
        return Response({'error': 'PeriodFilter not found'}, status=404)

    serializer = PeriodFilterAdminSerializer(periodfilter, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deletePeriodFilter(request, pk):
    try:
        periodfilter = PeriodFilter.objects.get(pk=pk)
    except PeriodFilter.DoesNotExist:
        return Response({'error': 'PeriodFilter not found'}, status=404)

    periodfilter.delete()
    return Response(status=204)


@api_view(['GET'])
def filterCategoriesList(request):
    filter_categories = FilterCategories.objects.all()
    serializer = FilterCategoriesAdminSerializer(filter_categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def filterCategoriesDetail(request, pk):
    filter_categories = FilterCategories.objects.get(pk=pk)
    serializer = FilterCategoriesAdminSerializer(filter_categories, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createFilterCategories(request):
    serializer = FilterCategoriesAdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def updateFilterCategories(request, pk):
    try:
        filter_categories = FilterCategories.objects.get(pk=pk)
    except FilterCategories.DoesNotExist:
        return Response({'error': 'FilterCategories not found'}, status=404)

    serializer = FilterCategoriesAdminSerializer(filter_categories, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deleteFilterCategories(request, pk):
    try:
        filter_categories = FilterCategories.objects.get(pk=pk)
    except FilterCategories.DoesNotExist:
        return Response({'error': 'FilterCategories not found'}, status=404)

    filter_categories.delete()
    return Response(status=204)



@api_view(['GET'])
def filtersList(request):
    filters = Filters.objects.all()
    serializer = FiltersAdminSerializer(filters, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def filtersDetail(request, pk):
    filters = Filters.objects.get(pk=pk)
    serializer = FiltersAdminSerializer(filters, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createFilters(request):
    serializer = FiltersAdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def updateFilters(request, pk):
    try:
        filters = Filters.objects.get(pk=pk)
    except Filters.DoesNotExist:
        return Response({'error': 'Filters not found'}, status=404)

    serializer = FiltersAdminSerializer(filters, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deleteFilters(request, pk):
    try:
        filters = Filters.objects.get(pk=pk)
    except Filters.DoesNotExist:
        return Response({'error': 'Filters not found'}, status=404)

    filters.delete()
    return Response(status=204)



@api_view(['GET'])
def provinceList(request):
    province = Province.objects.all()
    serializer = ProvinceAdminSerializer(province, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def provinceDetail(request, pk):
    province = Province.objects.get(pk=pk)
    serializer = ProvinceAdminSerializer(province, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createProvince(request):
    serializer = ProvinceAdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def updateProvince(request, pk):
    try:
        province = Province.objects.get(pk=pk)
    except Province.DoesNotExist:
        return Response({'error': 'Province not found'}, status=404)

    serializer = ProvinceAdminSerializer(province, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deleteProvince(request, pk):
    try:
        province = Province.objects.get(pk=pk)
    except Province.DoesNotExist:
        return Response({'error': 'Province not found'}, status=404)

    province.delete()
    return Response(status=204)

@api_view(['GET'])
def resourceList(request):
    resource = Resource.objects.all()
    serializer = ResourceAdminSerializer(resource, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def resourceDetail(request, pk):
    resource = Resource.objects.get(pk=pk)
    serializer = ResourceAdminSerializer(resource, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createResource(request):
    serializer = ResourceAdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def updateResource(request, pk):
    try:
        resource = Resource.objects.get(pk=pk)
    except Resource.DoesNotExist:
        return Response({'error': 'Resource not found'}, status=404)

    serializer = ResourceAdminSerializer(resource, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deleteResource(request, pk):
    try:
        resource = Resource.objects.get(pk=pk)
    except Resource.DoesNotExist:
        return Response({'error': 'Resource not found'}, status=404)

    resource.delete()
    return Response(status=204)







