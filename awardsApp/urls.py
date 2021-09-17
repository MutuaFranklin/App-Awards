from django.urls.conf import include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path, path, include


urlpatterns=[
   
    path('register/', views.register, name='register'),
    path('account/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    # re_path(r'publish/', views.publish_project, name='publish-project'),
    path('project-details/<int:id>', views.projectDetails, name='project-details'),


    path('publish-project/', views.publishProject, name='publish-project'),




    # path('login/', views.login_user, name='login'),


   


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


