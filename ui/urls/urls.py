from django.urls import path
from ui.views import index, UILoginView
from django.contrib.auth.views import LogoutView

# app_name = 'ui'

urlpatterns = [
    path('', index, name='index'),

    path(
        'login/',
        UILoginView.as_view(),
        name='login'
    ),

    path(
        'logout/',
        LogoutView.as_view(next_page='ui:login'),
        name='logout'
    ),
]
