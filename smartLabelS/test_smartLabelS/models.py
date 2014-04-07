from django.db import models
from django.utils.encoding import smart_unicode



# Create your models here.

class SignUp(models.Model):
    for_you = models.BooleanField(default=True, verbose_name="Yes I agree to the disclaimer")
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__ (self):
        return smart_unicode(self.email)
    
class Product(models.Model):
    product_id = models.IntegerField()
    product_name  = models.CharField(max_length=120, null=True, blank=True)
    max_temp = models.IntegerField()
    min_temp = models.IntegerField()
    
    def __unicode__ (self):
        return smart_unicode(self.product_name)
    
class Sites(models.Model):
    site_id = models.IntegerField()
    site_name = models.CharField(max_length=120, null=False, blank=False)
    
    def __unicode__ (self):
        return smart_unicode(self.site_name)
    
class Shipment(models.Model):
    shipment_id  =  models.IntegerField()#INTEGER PRIMARY KEY,
    prod_id = models.ForeignKey(Product, related_name='+')
    rfid_id_start = models.IntegerField()
    rfid_id_end = models.IntegerField()
    site_from  = models.ForeignKey(Sites, related_name='+')
    site_to  = models.ForeignKey(Sites, related_name='+')
    time_sent = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__ (self):
        return smart_unicode('%s %s %s %s' % (self.shipment_id, self.prod_id, self.rfid_id_start, self.rfid_id_end))
    
class ShipmentMonitor(models.Model):
    ship_id = models.ForeignKey(Shipment, related_name='+')
    timestamp = models.DateTimeField(auto_now_add=False, auto_now=True)
    temp  = models.IntegerField()
    loclong = models.FloatField()
    loclang = models.FloatField()
    leg_course = models.IntegerField()
    
    def __unicode__ (self):
        return smart_unicode(self.timestamp)
    
    
    
    
    
    