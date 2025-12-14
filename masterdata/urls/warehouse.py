from django.urls import path
from masterdata.views.warehouse import index

urlpatterns = [
    path('', index, name='index'),
]