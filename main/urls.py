from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


app_name = 'main'

urlpatterns = [
    path('', view_main, name='home'),
    path('generate', slug_generator, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
