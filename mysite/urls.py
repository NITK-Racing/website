from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'mysite'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.general ,name='contact'),
    path('team/', views.general ,name='about'),
    path('about/', views.general, name='about'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
