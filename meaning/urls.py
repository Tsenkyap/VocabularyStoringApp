from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wordmeaning.urls',namespace='wordmeaning')),
    path('accounts/', include('users.urls',namespace='users')),
]
