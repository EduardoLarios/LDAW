from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.new_donor, name='new_donor'),
    # url(r'^registrar/$', views.index, name='index'),
    url(r'^new_donor/$', views.new_donor, name='new_donor')
]
