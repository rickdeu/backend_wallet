from django.contrib import admin
from django.urls import path, include
from wallet import urls as wallet_url
from custom_user import url as user_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wallter/', include(wallet_url)),
    path('auth/', include(user_url))

]
