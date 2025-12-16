from django.urls import path
from masterdata.views.attribute_value import index

urlpatterns = [
    path('', index, name='index'),
]