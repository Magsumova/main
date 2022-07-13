from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import admin


urlpatterns = [
    path('', admin),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)