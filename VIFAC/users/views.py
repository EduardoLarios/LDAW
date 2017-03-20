from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from .models import User


class UserList(ListView):
    model = User
    template_name = "users/usuIndex.html"

class UserDetail(DetailView):
    model = User

class UserCreation(CreateView):
    model = User
    success_url = reverse_lazy('users:list')
    fields = ['name', 'password', 'username', 'aPaterno', 'aMaterno', 'fNacimiento', 'calle', 'colonia', 'cP']


class UserUpdate(UpdateView):
    model = User
    success_url = reverse_lazy('users:list')
    fields = ['name', 'password', 'username', 'aPaterno', 'aMaterno', 'fNacimiento', 'calle', 'colonia', 'cP']


class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('users:list')