from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.urls import path
# library 
# from admin_panel.crud.library import LibraryListCreate, LibraryRetrieveUpdateDestroy
from admin_panel.crud.library import create_library, list_libraries, delete_library, update_library
# library_cat 
# from admin_panel.crud.library_category import Library_CategoryListCreate, Library_CategoryRetrieveUpdateDestroy
from admin_panel.crud.library_category import create_library_category, list_library_categories, update_library_category, delete_library_category
# news
# from admin_panel.crud.news import NewsListCreate, NewsRetrieveUpdateDestroy
from admin_panel.crud.news import list_news, create_news, update_news, delete_news
# event 
# from admin_panel.crud.event import EventListCreate, EventRetrieveUpdateDestroy
from admin_panel.crud.event import create_event, list_events, update_event, delete_event
from admin_panel.crud.resources import categoryList, createCategory, categoryDetail, updateCategory, deleteCategory, \
    periodFilterList, periodFilterDetail, updatePeriodFilter, deletePeriodFilter, createPeriodFilter, \
    filterCategoriesList, filterCategoriesDetail, createFilterCategories, updateFilterCategories, \
    deleteFilterCategories, filtersList, filtersDetail, createFilters, updateFilters, deleteFilters, provinceList, \
    provinceDetail, createProvince, updateProvince, deleteProvince, resourceList, resourceDetail, createResource, \
    updateResource, deleteResource
# sliders 
# from admin_panel.crud.sliders import SlidersListCreate, SlidersRetrieveUpdateDestroy
from admin_panel.crud.sliders import list_sliders, create_slider, update_slider, delete_slider
# connection 
# from admin_panel.crud.connection import ConnectionListCreate, ConnectionRetrieveUpdateDestroy
from admin_panel.crud.connection import list_connections,  create_connection, delete_connection,  update_connection
# about 
# from admin_panel.crud.about import AboutListCreate, AboutRetrieveUpdateDestroy
from admin_panel.crud.about import create_about, update_about, delete_about, list_abouts
# feedback
# from admin_panel.crud.feedback import FeedbacksListCreate, FeedbacksRetrieveUpdateDestroy
from admin_panel.crud.feedback import list_feedbacks, create_feedback, update_feedback, delete_feedback
# comment 
# from admin_panel.crud.comment import CommentsListCreate, CommentsRetrieveUpdateDestroy
from admin_panel.crud.comment import create_comment, update_comment, list_comments, delete_comment
# resource 



urlpatterns = [
    # path('library_categories/', Library_CategoryListCreate.as_view(), name='library_category_list_create'),
    # path('library_categories/<int:pk>/', Library_CategoryRetrieveUpdateDestroy.as_view(), name='library_category_retrieve_update_destroy'),
    path('library_category/', list_library_categories, name='list_library_categories'),
    path('library_category/create/', create_library_category, name='create_library_category'),
    path('library_category/update/<int:pk>/', update_library_category, name='update_library_category'),
    path('library_category/delete/<int:pk>/', delete_library_category, name='delete_library_category'),



    # Library 
    # path('libraries/', LibraryListCreate.as_view(), name='library_list_create'),
    # path('libraries/<int:pk>/', LibraryRetrieveUpdateDestroy.as_view(), name='library_retrieve_update_destroy'),
    path('library/', list_libraries, name='list_libraries'),
    path('library/create/', create_library, name='create_library'),
    path('library/update/<int:pk>/', update_library, name='update_library'),
    path('library/delete/<int:pk>/', delete_library, name='delete_library'),



    # News
    # path('news/', NewsListCreate.as_view(), name='news_list_create'),
    # path('news/<int:pk>/', NewsRetrieveUpdateDestroy.as_view(), name='news_retrieve_update_destroy'),
    path('news/', list_news, name='list_news'),
    path('news/create/', create_news, name='create_news'),
    path('news/update/<int:pk>/', update_news, name='update_news'),
    path('news/delete/<int:pk>/', delete_news, name='delete_news'),


    # event 
    # path('events/', EventListCreate.as_view(), name='event_list_create'),
    # path('events/<int:pk>/', EventRetrieveUpdateDestroy.as_view(), name='event_retrieve_update_destroy'),\
    path('event/', list_events, name='list_events'),
    path('event/create/', create_event, name='create_event'),
    path('event/update/<int:pk>/', update_event, name='update_event'),
    path('event/delete/<int:pk>/', delete_event, name='delete_event'),
    

    # sliders
    # path('sliders/', SlidersListCreate.as_view(), name='sliders_list_create'),
    # path('sliders/<int:pk>/', SlidersRetrieveUpdateDestroy.as_view(), name='sliders_retrieve_update_destroy'),
    path('sliders/', list_sliders, name='list_sliders'),
    path('sliders/create/', create_slider, name='create_slider'),
    path('sliders/update/<int:pk>/', update_slider, name='update_slider'),
    path('sliders/delete/<int:pk>/', delete_slider, name='delete_slider'),


    # connection 
    # path('connections/', ConnectionListCreate.as_view(), name='connection_list_create'),
    # path('connections/<int:pk>/', ConnectionRetrieveUpdateDestroy.as_view(), name='connection_retrieve_update_destroy'),
    path('connections/', list_connections, name='list-connections'),
    path('connections/create/', create_connection, name='create-connection'),
    path('connections/update/<int:pk>/', update_connection, name='update-connection'),
    path('connections/delete/<int:pk>/', delete_connection, name='delete-connection'),


    # About 
    # path('about/', AboutListCreate.as_view(), name='about_list_create'),
    # path('about/<int:pk>/', AboutRetrieveUpdateDestroy.as_view(), name='about_retrieve_update_destroy'),
    path('about/', list_abouts, name='list_abouts'),
    path('about/create/', create_about, name='create_about'),
    path('about/update/<int:pk>/', update_about, name='update_about'),
    path('about/delete/<int:pk>/', delete_about, name='delete_about'),


    # Feedback
    # path('feedbacks/', FeedbacksListCreate.as_view(), name='feedbacks_list_create'),
    # path('feedbacks/<int:pk>/', FeedbacksRetrieveUpdateDestroy.as_view(), name='feedbacks_retrieve_update_destroy'),
    path('feedback/', list_feedbacks, name='list_feedbacks'),
    path('feedback/create/', create_feedback, name='create_feedback'),
    path('feedback/update/<int:pk>/', update_feedback, name='update_feedback'),
    path('feedback/delete/<int:pk>/', delete_feedback, name='delete_feedback'),



    # Comment
    # path('comments/', CommentsListCreate.as_view(), name='comments_list_create'),
    # path('comments/<int:pk>/', CommentsRetrieveUpdateDestroy.as_view(), name='comments_retrieve_update_destroy'),
    path('comment/', list_comments, name='list_comments'),
    path('comment/create/', create_comment, name='create_comment'),
    path('comment/update/<int:pk>/', update_comment, name='update_comment'),
    path('comment/delete/<int:pk>/', delete_comment, name='delete_comment'),

    #Resource   category
    path('category/',categoryList,name='cat-list'),
    path('category/<int:pk>/detail/',categoryDetail,name='cat-detail'),
    path('category/<int:pk>/update/',updateCategory,name='cat-update'),
    path('category/<int:pk>/delete/',deleteCategory,name='cat-delete'),
    path('category/create/',createCategory,name='cat-create'),

    # Resource periodfilter
    path('period_filter/',periodFilterList,name='period-filter-list'),
    path('period_filter/<int:pk>/detail/',periodFilterDetail,name='period-filter-detail'),
    path('period_filter/<int:pk>/update/',updatePeriodFilter,name='period-filter-update'),
    path('period_filter/<int:pk>/delete/',deletePeriodFilter,name='period-filter-delete'),
    path('period_filter/create/',createPeriodFilter,name='period-filter-create'),

    # Resource filter-category
    path('filter_category/', filterCategoriesList, name='filter-category-list'),
    path('filter_category/<int:pk>/detail/', filterCategoriesDetail, name='filter-category-detail'),
    path('filter_category/create/', createFilterCategories, name='filter-category-create'),
    path('filter_category/<int:pk>/update/', updateFilterCategories, name='filter-category-update'),
    path('filter_category/<int:pk>/delete/', deleteFilterCategories, name='filter-category-delete'),

    # Resource filters
    path('filters/', filtersList, name='filters-list'),
    path('filters/<int:pk>/detail/', filtersDetail, name='filters-detail'),
    path('filters/create/', createFilters, name='filters-create'),
    path('filters/<int:pk>/update/', updateFilters, name='filters-update'),
    path('filters/<int:pk>/delete/', deleteFilters, name='filters-delete'),

    # Resource province
    path('province/', provinceList, name='province-list'),
    path('province/<int:pk>/detail/', provinceDetail, name='province-detail'),
    path('province/create/', createProvince, name='province-create'),
    path('province/<int:pk>/update/', updateProvince, name='province-update'),
    path('province/<int:pk>/delete/', deleteProvince, name='province-delete'),

    # Resource
    path('resource/', resourceList, name='resource-list'),
    path('resource/<int:pk>/detail/', resourceDetail, name='resource-detail'),
    path('resource/create/', createResource, name='resource-create'),
    path('resource/<int:pk>/update/', updateResource, name='resource-update'),
    path('resource/<int:pk>/delete/', deleteResource, name='resource-delete'),
]
