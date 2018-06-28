# coding: utf-8


from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from snippets.views import SnippetViewSet, UserViewSets


router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSets)


urlpatterns = [
    url(r'^', include(router.urls))        
]
