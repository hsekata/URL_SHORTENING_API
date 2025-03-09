from django.urls import path
from .views import *
urlpatterns = [
    path("shorten", CreateShortendedURL),
    path("shorten/<str:shortcode>", RetrieveUpdateDestroyURLView.as_view()),
    path("shorten/<str:shortcode>/stat", RetrieveStatView.as_view()),
    # path("shorten/<str:shortcode>/put", UpdateURLView.as_view()),
]