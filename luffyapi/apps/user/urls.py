from django.urls import path,include,re_path
from user import views
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('',views.LoginView,'login')
urlpatterns = [
    path('',include(router.urls))
]