from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('autenticacion.urls')),
    path('board/', include('board.urls')),
    path('surveys/', include('djf_surveys.urls'))
]
