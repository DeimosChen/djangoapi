
import xadmin
xadmin.autodiscover()
from xadmin.plugins import xversion
from django.urls import path,include,re_path
from django.conf import settings
from django.views.static import serve
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('home/', include('home.urls')),
    path('user/', include('user.urls')),
    re_path('media/(?P<path>.*)',serve,{'document_root':settings.MEDIA_ROOT})
]
