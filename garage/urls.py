from django.contrib.auth.decorators import login_required
from django.urls import path

from garage import views

urlpatterns = [
    path('api/vehicle_list', login_required(views.api_vehicle_list), name='api_vehicle_list'),
    path('vehicle_list', login_required(views.VehicleList.as_view()), name='vehicle_list'),
    path('vehicle_new', login_required(views.VehicleCreate.as_view()), name='vehicle_new'),
    path('vehicle_edit/<int:pk>/', login_required(views.VehicleUpdate.as_view()), name='vehicle_edit'),
    path('vehicle_delete/<int:pk>/', login_required(views.VehicleDelete.as_view()), name='vehicle_delete'),
    path('buy_vehicle/<int:id>/', login_required(views.buy_vehicle), name='buy_vehicle'),
]
