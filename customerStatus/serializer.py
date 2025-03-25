from rest_framework import serializers
from .models import CreateCustomer , CustomerStatus , CustomerDiseases

class CreateCustomerSerializer(serializers.ModelSerializer):
    class Meta :
        model = CreateCustomer
        fields = ['id' ,'user_name' , 'last_name' , 'age' , 'job' , 'education_degree' , 'economic_status' , 'phone_number' , 'address' , 'work_address'] 


class CustomerStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerStatus
        fields = ['related_to' , 'health_now' , 'last_examination' , 'is_under_care_now' , 'have_surgery' , 'have_blood_pressure' , 'have_sugar' , 'bee_hospitalization' , 'have_allergy' , 'used_milicent' , 'description']

class CustomerDiseasesSerializer(serializers.ModelSerializer):
    class Meta :
        model = CustomerDiseases
        fields = ['related_to' , 'heart_attack' , 'pacemaker' , 'stroke' , 'nervous_disorder' , 'asthma' , 'epilepsy' , 'kidney_disorder' , 'liver_disorder' , 'addiction' , 'tuberculosis' , 'stomach_ulcer' , 'allergy' , 'aids' , 'hepatitis' , 'insomnia' , 'cancer' , 'radiotherapy' , 'women_pregnancy']