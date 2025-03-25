from rest_framework import serializers
from .models import FactorItems , TreatmentFactor , PlaneItems , TreatmentPlane

class TreatmentPlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentPlane
        fields =  ["created_at" , "related_to"]

class TreatmentPlaneItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaneItems
        fields = ['id' , "teeth_problem" , 'teeth_number' ]


class TreatmentFactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentFactor
        fields =  ["created_at" , "related_to"]


class TreatmentFactorItemsSerializer(serializers.ModelSerializer):
    # customer_id = TreatmentFactorSerializer()
    class Meta:
        model = FactorItems
        fields = ['id' , "teeth_problem" , 'teeth_number' , 'date' , 'price' , 'payment' , 'remainder' ]
  
class PostTreatmentPlaneItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaneItems
        fields = ['id' , "teeth_problem" , 'teeth_number' , 'related_to' ]

class PostTreatmentFactorItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactorItems
        fields = ['id' , "teeth_problem" , 'teeth_number' , 'date' , 'price' , 'payment' , 'related_to' , 'remainder' ]
  