from .models import CreateCustomer , CustomerStatus , CustomerDiseases
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_list_or_404 , get_object_or_404
from .serializer import CreateCustomerSerializer , CustomerStatusSerializer , CustomerDiseasesSerializer
from rest_framework import status 

# CustomerProfile
@api_view(["GET" , "POST"])
def get_post_customer(request):
    if request.method == "GET":
        queryset = CreateCustomer.objects.all()
        serializer = CreateCustomerSerializer(queryset , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    elif request.method == "POST" :
        serializer = CreateCustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

@api_view(['PUT' , "DELETE" , "GET"])
def put_delete_customer(request , id):
    customer = get_object_or_404(CreateCustomer , id=id)
    if request.method == 'PUT' :
        serializer = CreateCustomerSerializer(customer , data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE" : 
        customer.delete()
        return Response(status=status.HTTP_200_OK)
    elif request.method == "GET":
        serializer = CreateCustomerSerializer(customer)
        return Response(serializer.data)


 # CustomerStatus
@api_view(['GET' , "POST"])
def get_post_customer_status(request):
    if request.method == 'GET':
        queryset = CustomerStatus.objects.all().select_related('related_to')
        serializer = CustomerStatusSerializer(queryset , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CustomerStatusSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    
@api_view(['PUT' , "GET"])
def update_customer_status(request , id):
    customer_status = get_object_or_404(CustomerStatus , pk=id)
    if request.method == "PUT":
        serializer = CustomerStatusSerializer(customer_status , data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "GET" :
        serializer = CustomerStatusSerializer(customer_status)
        return Response(serializer.data)
    
    
# Customer Diseases

@api_view(['GET' , 'POST'])
def get_post_customer_diseases(request):
    if request.method == "GET":
        queryset = CustomerDiseases.objects.all().select_related('related_to')
        serializer = CustomerDiseasesSerializer(queryset , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = CustomerDiseasesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    


@api_view(['PUT' , "GET"])
def update_customer_diseases(request , id):
    customer_diseases = get_object_or_404(CustomerDiseases , pk=id)
    if request.method == "PUT":
        serializer = CustomerDiseasesSerializer(customer_diseases , data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "GET" :
        serializer = CustomerDiseasesSerializer(customer_diseases)
        return Response(serializer.data)
    
    