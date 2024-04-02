from django.urls import path
from api.view.other_app import LibrariesListViews, LibraryCategoryListViews, AboutListViews, CommentListViews, ConnectionListViews, EventListViews, FeedbackListViews, NewsListViews, SlidersListViews

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
]
