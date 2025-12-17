from django.urls import path, include

# from .user import urlpatterns as user_urls
# from .unit import urlpatterns as unit_urls
# from .attribute import urlpatterns as attribute_urls
# from .warehouse import urlpatterns as warehouse_urls
# from .payment_method import urlpatterns as paymentmethod_urls
# from .attribute_value import urlpatterns as attribute_value_urls

urlpatterns = [
    # path('', include((user_urls, 'user'))),
    path('units/', include('masterdata.urls.unit')),
]