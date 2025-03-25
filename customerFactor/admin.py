from django.contrib import admin
from .models import PlaneItems , TreatmentPlane , FactorItems , TreatmentFactor
# Register your models here.


@admin.register(PlaneItems)
class PlaneAdmin(admin.ModelAdmin):
    list_display = ['id' , 'teeth_number' , 'teeth_problem']



@admin.register(TreatmentPlane)
class PlaneAdmin(admin.ModelAdmin):
    list_display = ['created_at' , 'related_to']


@admin.register(FactorItems)
class PlaneAdmin(admin.ModelAdmin):
    list_display = ['id' , 'teeth_number' , 'teeth_problem']



@admin.register(TreatmentFactor)
class PlaneAdmin(admin.ModelAdmin):
    list_display = ['created_at' , 'related_to']



