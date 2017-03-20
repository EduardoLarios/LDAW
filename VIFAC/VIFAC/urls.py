
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^usuarios/', include('users.urls', namespace="users")),
    url(r'^donadores/', include('donors.urls')),
    url(r'^admin/', admin.site.urls),
]
