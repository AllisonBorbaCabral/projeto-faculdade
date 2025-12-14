from django.urls import path
from masterdata.views.unit import index

urlpatterns = [
    path('', index, name='index'),
]