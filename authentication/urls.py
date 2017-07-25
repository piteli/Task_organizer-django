from django.conf.urls import url, include
from .views import LoginController, RegisterController
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', LoginController.as_view(), name='login'),
    url(r'^register/$', RegisterController.as_view(),  name='register'),
    url(r'logout/$', auth_views.logout,{'next_page':'home:index'}, name='logout'),
]
