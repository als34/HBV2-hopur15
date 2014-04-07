from django.contrib import admin


# Register your models here.
from .models import SignUp, Sites, Product, Shipment, ShipmentMonitor

class SignUpAdmin(admin.ModelAdmin):
    class Meta:
        model = SignUp

class SitiesAdmin(admin.ModelAdmin):
    class Meta:
        model = Sites

class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product

class ShipmentAdmin(admin.ModelAdmin):
    class Meta:
        model = Shipment

class ShipmentMonitorAdmin(admin.ModelAdmin):
    class Meta:
        model = ShipmentMonitor

        
admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Sites, SitiesAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Shipment, ShipmentAdmin)
admin.site.register(ShipmentMonitor, ShipmentMonitorAdmin)