from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from core.forms import SignUpForm
from core.models import User
from garage.models import Vehicle


def index(request):
    users_list = []
    vehicles_list = []
    garage = []
    if not request.user.is_superuser:
        vehicles = Vehicle.objects.filter(owner=None)
        garage = Vehicle.objects.filter(owner=request.user).all()
        if vehicles:
            for vehicle in vehicles_list:
                vehicles_list.append({
                    'name': vehicle.name,
                    'type': vehicle.type,
                    'color': vehicle.color,
                    'year': vehicle.year,
                    'price': vehicle.price,
                    'icon': vehicle.icon
                })

    else:
        users = User.objects.filter(Q(is_superuser=False))
        vehicles = Vehicle.objects.all()
        if users:
            for user in users:
                users_list.append({
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'phone': user.phone,
                    'balance': user.balance,
                })
        if vehicles:
            for vehicle in vehicles_list:
                vehicles_list.append({
                    'name': vehicle.name,
                    'type': vehicle.type,
                    'color': vehicle.color,
                    'year': vehicle.year,
                    'price': vehicle.price,
                    'icon': vehicle.icon
                })

    return render(request, 'core/index.html', {'users': users_list, 'vehicles': vehicles_list, 'garage': garage})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')

        return render(request, 'register.html', {'form': form})

    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})


class UsersList(ListView):
    model = User

    def get_queryset(self):
        users = []
        if self.request.user.is_superuser:
            users = User.objects.filter(Q(is_superuser=False))
        return users


class UserUpdate(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'phone', 'balance']
    success_url = reverse_lazy('users_list')

    def get_context_data(self, **kwargs):
        context = super(UserUpdate, self).get_context_data(**kwargs)
        context['is_create'] = False
        return context

