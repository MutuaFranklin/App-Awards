from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

from django.urls import re_path, path, include


urlpatterns=[

    path('<username>/', views.userProfile, name='userProfile'),



]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)












   