from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('signup', views.signnewuser, name='signnewuser'),
    path('login', views.loginuser, name='loginuser'),
    path('logout', views.logoutuser , name='logoutuser'),
]



# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)