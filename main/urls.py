from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', view_main, name='home'),
    path('shot-url', short_url, name='home'),
    path('get-info', get_count_url_visits, name='visits'),
    path('<slug:slug>', url_redirect, name='redirect'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
