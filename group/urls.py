from django.urls import path

from group.views import GroupCreateView, ListGroupView


urlpatterns = [
    path('group/', ListGroupView.as_view(), name='list-group'),
    path('group/add/', GroupCreateView.as_view(), name='create-group')
]
