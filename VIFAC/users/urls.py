from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^registrar/$', views.index, name='index'),
	url(r'^modificar/$', views.modificar, name='modificar'),
	url(r'^borrar/', views.borrar, name='borrar'),
	url(r'^consultar/', views.consultar, name='consultar')
]
