from django.urls import path
from masterdata.views.paymentmethod import index

urlpatterns = [
    path('', index, name='index'),
]