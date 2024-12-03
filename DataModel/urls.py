
from django.conf.urls import *
from .views import*

urlpatterns = [
    url(r'fields/$',FieldListCreateView.as_view(),name='field-create-list'),
    url(r'fields/(?P<pk>\d+)/$',FieldRetrieveUpdateView.as_view(),name='field-update-retrieve'),
]
