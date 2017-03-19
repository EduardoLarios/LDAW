from django.conf.urls import url
from . import views


app_name = 'users'

urlpatterns = [
	url(r'^registrar/$', views.UserFormView.as_view(), name='register')
]