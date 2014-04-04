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
    
    
    
class CreateF(models.Model):
    shipment_nr = models.CharField(max_length= 30, null=False, blank=False)
    first_nr = models.CharField(max_length = 30, null=False, blank = False)
    quantity = models.CharField(max_length =10, null =False, blank = False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__ (self):
        return '%s %s %s ' % (self.shipment_nr, self.first_nr, self.quantity)
    

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)