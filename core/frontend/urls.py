from django.conf.urls import include, url
from django.conf.urls.static import static
from django.urls import path
from frontend import views
#from .views import (IndexView)

urlpatterns = [
    url(r'^index/', views.IndexView.as_view(), name='index'),
    url(r'^index/spotCreate/', views.IndexView.as_view(), name='spotCreate')    
#    url(r'^map/', views.MapView.as_view(), name='map')
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
