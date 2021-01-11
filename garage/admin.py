from django.contrib import admin
from .models import Vehicle


class VehicleAdmin(admin.ModelAdmin):
    fields = ['owner', 'name', 'type', 'color', 'year', 'price', 'icon']
    list_display = ('owner', 'name', 'type', 'color', 'year', 'price', 'icon')


admin.site.register(Vehicle, VehicleAdmin)
