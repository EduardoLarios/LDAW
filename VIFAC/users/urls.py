from django.conf.urls import url
from .views import (
    UserList,
    UserDetail,
    UserCreation,
    UserUpdate,
    UserDelete
)

urlpatterns = [
    url(r'^$', UserList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', UserDetail.as_view(), name='detail'),
    url(r'^nuevo$', UserCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', UserUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', UserDelete.as_view(), name='delete'),
]