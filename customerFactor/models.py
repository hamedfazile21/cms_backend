from django.db import models
from customerStatus.models import CreateCustomer

class TreatmentPlane(models.Model):
    created_at = models.DateField(auto_now_add=True)
    related_to = models.OneToOneField(CreateCustomer , on_delete=models.CASCADE , primary_key=True)

    
class PlaneItems(models.Model):
    teeth_number = models.CharField(max_length=255)
    teeth_problem = models.CharField(max_length=255)
    related_to = models.ForeignKey(TreatmentPlane , on_delete=models.CASCADE , related_name="items")

    
    
class TreatmentFactor(models.Model):
    created_at = models.DateField(auto_now_add=True)
    related_to = models.OneToOneField(CreateCustomer , on_delete=models.CASCADE , primary_key=True)


class FactorItems(models.Model):
    teeth_number = models.CharField(max_length=255)
    teeth_problem = models.CharField(max_length=255)
    price = models.IntegerField()
    payment = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    related_to = models.ForeignKey(TreatmentFactor , on_delete=models.CASCADE, related_name="factor")
    remainder = models.IntegerField()
