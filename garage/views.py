from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from garage.models import Vehicle


@csrf_exempt
def api_vehicle_list(request):
    if request.user.is_superuser:
        vehicles = list(Vehicle.objects.all().values())
    else:
        vehicles = list(Vehicle.objects.filter(owner=request.user).values())
    return JsonResponse(vehicles, safe=False)


class VehicleList(ListView):
    model = Vehicle

    def get_queryset(self):
        if self.request.user.is_superuser:
            vehicle = Vehicle.objects.all()
        else:
            vehicle = Vehicle.objects.filter(owner=None)
        return vehicle


class VehicleCreate(CreateView):
    model = Vehicle
    fields = ['owner', 'name', 'type', 'color', 'year', 'price', 'icon']
    success_url = reverse_lazy('vehicle_list')

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(VehicleCreate, self).get_context_data(**kwargs)
        context['is_create'] = True
        return context


class VehicleUpdate(UpdateView):
    model = Vehicle
    fields = ['owner', 'name', 'type', 'color', 'year', 'price', 'icon']
    success_url = reverse_lazy('vehicle_list')

    def get_context_data(self, **kwargs):
        context = super(VehicleUpdate, self).get_context_data(**kwargs)
        context['is_create'] = False
        return context


class VehicleDelete(DeleteView):
    model = Vehicle
    success_url = reverse_lazy('vehicle_list')


def buy_vehicle(request, id):
    vehicle = Vehicle.objects.get(id=id)
    if request.user.balance > vehicle.price:
        request.user.balance = request.user.balance - vehicle.price
        request.user.save()
        vehicle.owner = request.user
        vehicle.save()
        message = 'Vehicle successfully bought! Your balance is now ' + str(request.user.balance)
    else:
        message = 'Not enough money to buy this vehicle.'
    return render(request, 'garage/shop_vehicle.html', {'message': message})
