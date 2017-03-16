from django.conf.urls import url
from . import views

urlpatterns = [
    
    # url(r'^registrar/$', views.index, name='index'),

    url(r'^$', views.index, name='index'),
    url(r'^donadores/$', views.new_donor, name='new_donor'),
    url(r'^donaciones/$', views.new_donation, name='new_donation')
]
