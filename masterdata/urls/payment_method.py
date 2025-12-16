from django.urls import path
from masterdata.views.payment_method import index

urlpatterns = [
    path('', index, name='index'),
]