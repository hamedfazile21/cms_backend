from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.CreateCustomer)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name' , 'last_name' , 'job' , 'education_degree' , 'economic_status' , 'phone_number' , 'address' , 'work_address']


@admin.register(models.CustomerStatus)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['related_to', 'health_now' , 'last_examination' , 'is_under_care_now' , 'have_surgery' , 'have_blood_pressure' , 'have_sugar' , 'bee_hospitalization' , 'have_allergy' , 'used_milicent' ,'description']
    
    
    
    
@admin.register(models.CustomerDiseases)
class CustomerDiseases(admin.ModelAdmin):
    list_display = ['related_to' , 'heart_attack']