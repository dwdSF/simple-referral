from django.urls import path

from .views import login_view, verify_view


urlpatterns = [
    path('', login_view, name='login-view'),
    path('verify/', verify_view, name='verify-view'),
]
