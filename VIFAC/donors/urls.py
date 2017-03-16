from django.conf.urls import url
from . import views

urlpatterns = [
    
    # url(r'^registrar/$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^new_donor/$', views.new_donor, name='new_donor'),
    url(r'^new_donation/$', views.new_donation, name='new_donation')
]
