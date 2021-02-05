from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('referral.urls')),
    path('', include('accounts.urls')),
    path('', include('django.contrib.auth.urls')),
]
