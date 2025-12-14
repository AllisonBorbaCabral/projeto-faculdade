from django.urls import path
from masterdata.views.attribute import index

urlpatterns = [
    path('', index, name='index'),
]