from django.conf.urls import url

from . import views
from .views import UserDelete


app_name = 'users'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^registrar/$', views.UserFormView.as_view(), name='register'),
    url(r'^borrar/(?P<pk>\d+)$', UserDelete.as_view(), name='delete'),
    url(r'^lista_usuarios/$', views.list_users, name='lista_usuarios'),
    url(r'^editar_usuario/(?P<pk>\d+)/$', views.UserUpdate.as_view(), name="user-update"),
]