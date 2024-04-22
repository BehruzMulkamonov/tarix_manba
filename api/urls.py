from django.urls import path
from api.view.other_app import LibrariesListViews, LibraryCategoryListViews, AboutListViews, CommentListViews, \
    ConnectionListViews, EventListViews, FeedbackListViews, NewsListViews, SlidersListViews
from api.view.resources import categoryListView, categoryDetailView, periodFilterListView, periodFilterDetailView, \
    filterCategoriesListView, filterCategoriesDetailView, filtersListView, filtersDetailView, provinceListView, \
    provinceDetailView, resourceListView, resourceDetailView

urlpatterns = [
    path('library/', LibrariesListViews.as_view()),
    path('library_cat/', LibraryCategoryListViews.as_view()),
    path('about/', AboutListViews.as_view()),
    path('even/', EventListViews.as_view()),
    path('news/', NewsListViews.as_view()),
    path('slider/', SlidersListViews.as_view()),
    path('comment/', CommentListViews.as_view()),
    path('feedback/', FeedbackListViews.as_view()),
    path('connection/', ConnectionListViews.as_view()),

    # Resources   url
    # category
    path('category_api-list', categoryListView, name='category-list'),
    path('category_api-detail/<int:pk>/', categoryDetailView, name='category-detail'),

    # period_filter
    path('period_api-list', periodFilterListView, name='period_api-list'),
    path('period_api-detail/<int:pk>/', periodFilterDetailView, name='period_api-detail'),

    # filter_categories
    path('filter_categories_api-list', filterCategoriesListView, name='filter_categories_api-list'),
    path('filter_categories_api-detail/<int:pk>/', filterCategoriesDetailView, name='filter_categories_api-detail'),

    # filters
    path('filters_api-list', filtersListView, name='filters_api-list'),
    path('filters_api-detail/<int:pk>/', filtersDetailView, name='filters_api-detail'),

    # province
    path('province_api-list', provinceListView, name='province_api-list'),
    path('province_api-detail/<int:pk>/', provinceDetailView, name='province_api-detail'),

    # resource
    path('resource_api-list', resourceListView, name='resource_api-list'),
    path('resource_api-detail/<int:pk>/', resourceDetailView, name='resource_api-detail'),
]
