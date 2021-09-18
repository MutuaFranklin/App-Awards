from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from .views  import UpdateProfileView
from django.urls import re_path, path


urlpatterns=[

    path('<username>/', views.userProfile, name='userProfile'),
    path('update/<int:pk>', UpdateProfileView.as_view(), name='update-profile'), 



]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)












   