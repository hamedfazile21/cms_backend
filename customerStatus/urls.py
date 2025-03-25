from .views import get_post_customer , put_delete_customer , get_post_customer_status , update_customer_status , get_post_customer_diseases , update_customer_diseases
from django.urls import path

urlpatterns = [
    path('customer_profile/' , get_post_customer),
    path('customer_profile_id/<int:id>/' , put_delete_customer),
    path('customer_status/' , get_post_customer_status),
    path('customer_status_id/<int:id>/' , update_customer_status),
    path('customer_diseases/' , get_post_customer_diseases),
    path('customer_diseases_id/<int:id>/' ,update_customer_diseases),
]