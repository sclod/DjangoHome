from django.urls import path

from group.views import create_group


urlpatterns = [
    path('create_group/', create_group)
]
