from rest_framework import routers
from django.urls import include, path
from .views import RegexViewSet, TagsViewSet, SingleRegexViewSet

urlpatterns = [
    path('regex/', RegexViewSet.as_view()),
    path('regex/<str:pk>', SingleRegexViewSet.as_view()),
    path('tags/', TagsViewSet.as_view()),
]
