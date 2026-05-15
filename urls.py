from django.urls import path
from .views import register_user, PaperUploadView, ReviewCreateView, PaperListView
from .views import ReviewCreateView


urlpatterns = [
    path('register/', register_user),
    path('upload/', PaperUploadView.as_view()),
    path('review/', ReviewCreateView.as_view()),
    path('papers/', PaperListView.as_view()),
]
