from django.shortcuts import render
from .models import PlaneItems , TreatmentPlane , FactorItems , TreatmentFactor
from .serializers import TreatmentFactorItemsSerializer , PostTreatmentFactorItemsSerializer , TreatmentPlaneItemsSerializer ,PostTreatmentPlaneItemsSerializer, TreatmentPlaneSerializer , TreatmentPlaneSerializer , TreatmentFactorSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response 
from rest_framework.generics import RetrieveUpdateDestroyAPIView 

class TreatmentAccess(RetrieveUpdateDestroyAPIView):
    lookup_field = "id" 

    def get_queryset(self):
        customer_id = self.kwargs.get("customer_id")  
        item_id = self.kwargs.get("id")  
        name = self.kwargs.get('name')
        if name == 'plane' :
            try:
             treatment_plane = TreatmentPlane.objects.get(related_to=customer_id)
            except TreatmentPlane.DoesNotExist:
                return PlaneItems.objects.none()  
            return PlaneItems.objects.filter(related_to=treatment_plane, id=item_id)    
        elif name == "factor":
            try:
             treatment_factor = TreatmentFactor.objects.get(related_to=customer_id)
            except TreatmentFactor.DoesNotExist:
                return FactorItems.objects.none()  
            return FactorItems.objects.filter(related_to=treatment_factor, id=item_id)    

    def get_serializer_class(self):
        name = self.kwargs.get('name')
        if name == 'plane':
            return TreatmentPlaneItemsSerializer
        elif name == 'factor':
            return TreatmentFactorItemsSerializer
    
        
@api_view(['GET'])
def treatment_plane_detail(request, id):
    try:
        treatment_plane = TreatmentPlane.objects.get(related_to=id)
        treatment_factor = TreatmentFactor.objects.get(related_to=id)
        planeItems = PlaneItems.objects.filter(related_to=treatment_plane)
        factorItems = FactorItems.objects.filter(related_to=treatment_factor)

        customer_data = TreatmentPlaneSerializer(treatment_plane)
        plane_items_data = TreatmentPlaneItemsSerializer(planeItems, many=True) 
        factor_items_data = TreatmentFactorItemsSerializer(factorItems , many=True)

        return Response({
            "customer": customer_data.data,
            "plans": plane_items_data.data,
            "factor" : factor_items_data.data
        })
    except TreatmentPlane.DoesNotExist:
        return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)
        

@api_view(['POST'])
def post_items_treatment(request , name):
    if name == "plane" :
        serializer = PostTreatmentPlaneItemsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif name == "factor" :
        serializer = PostTreatmentFactorItemsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data) 
    
    
@api_view(['POST'])
def post_treatment(request , name):
    if name == "plane":
        serializer = TreatmentPlaneSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif name == 'factor':
        serializer = TreatmentFactorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)