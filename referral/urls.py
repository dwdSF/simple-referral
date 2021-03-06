from django.urls import path

from .views import invite_activation, profile_view, referrer_profile

urlpatterns = [
    path('', profile_view, name='profile-view'),
    path('invite/', invite_activation, name='invite'),
    path('<str:code>/', referrer_profile, name='refprofile-view'),
]
