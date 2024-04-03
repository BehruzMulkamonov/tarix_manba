from django.urls import path, include
from rest_framework.routers import DefaultRouter

# library
from admin_panel.crud.library import LibraryListCreate, LibraryRetrieveUpdateDestroy
# library_cat 
from admin_panel.crud.library_category import Library_CategoryListCreate, Library_CategoryRetrieveUpdateDestroy
# news
from admin_panel.crud.news import NewsListCreate, NewsRetrieveUpdateDestroy
# event 
from admin_panel.crud.event import EventListCreate, EventRetrieveUpdateDestroy
from admin_panel.crud.resources import CategoryModelViewSet
# sliders 
from admin_panel.crud.sliders import SlidersListCreate, SlidersRetrieveUpdateDestroy
# connection 
from admin_panel.crud.connection import ConnectionListCreate, ConnectionRetrieveUpdateDestroy
# about 
from admin_panel.crud.about import AboutListCreate, AboutRetrieveUpdateDestroy
# feedback
from admin_panel.crud.feedback import FeedbacksListCreate, FeedbacksRetrieveUpdateDestroy
# comment 
from admin_panel.crud.comment import CommentsListCreate, CommentsRetrieveUpdateDestroy


router = DefaultRouter()
router.register("api/v1/categoryapi/", CategoryModelViewSet, basename='category')


urlpatterns = [
    path('library_categories/', Library_CategoryListCreate.as_view(), name='library_category_list_create'),
    path('library_categories/<int:pk>/', Library_CategoryRetrieveUpdateDestroy.as_view(), name='library_category_retrieve_update_destroy'),


    # Library 
    path('libraries/', LibraryListCreate.as_view(), name='library_list_create'),
    path('libraries/<int:pk>/', LibraryRetrieveUpdateDestroy.as_view(), name='library_retrieve_update_destroy'),



    # News
    path('news/', NewsListCreate.as_view(), name='news_list_create'),
    path('news/<int:pk>/', NewsRetrieveUpdateDestroy.as_view(), name='news_retrieve_update_destroy'),


    # event 
    path('events/', EventListCreate.as_view(), name='event_list_create'),
    path('events/<int:pk>/', EventRetrieveUpdateDestroy.as_view(), name='event_retrieve_update_destroy'),\
    

    # sliders
    path('sliders/', SlidersListCreate.as_view(), name='sliders_list_create'),
    path('sliders/<int:pk>/', SlidersRetrieveUpdateDestroy.as_view(), name='sliders_retrieve_update_destroy'),


    # connection 
    path('connections/', ConnectionListCreate.as_view(), name='connection_list_create'),
    path('connections/<int:pk>/', ConnectionRetrieveUpdateDestroy.as_view(), name='connection_retrieve_update_destroy'),


    # About 
    path('about/', AboutListCreate.as_view(), name='about_list_create'),
    path('about/<int:pk>/', AboutRetrieveUpdateDestroy.as_view(), name='about_retrieve_update_destroy'),


    # Feedback
    path('feedbacks/', FeedbacksListCreate.as_view(), name='feedbacks_list_create'),
    path('feedbacks/<int:pk>/', FeedbacksRetrieveUpdateDestroy.as_view(), name='feedbacks_retrieve_update_destroy'),


    # Comment
    path('comments/', CommentsListCreate.as_view(), name='comments_list_create'),
    path('comments/<int:pk>/', CommentsRetrieveUpdateDestroy.as_view(), name='comments_retrieve_update_destroy'),

    #Resource
    path("", include(router.urls)),

]
