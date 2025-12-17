from django.urls import path
from masterdata.views.unit import unit_list, unit_add

app_name = 'unit'

urlpatterns = [
    path('', unit_list, name='list'),
    path('unit-add/', unit_add, name='add'),
]