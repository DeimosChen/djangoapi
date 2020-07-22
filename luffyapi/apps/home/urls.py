from django.urls import path,include,re_path
from home import views
urlpatterns = [
    path('banner/',views.Banner.as_view())
]