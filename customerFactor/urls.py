from .views import treatment_plane_detail , post_items_treatment , TreatmentAccess  , post_treatment
from django.urls import path

urlpatterns = [
    path('customer-treatment/<int:id>/' , treatment_plane_detail),
    path('customer-treatment/<int:customer_id>/<name>/<int:id>/' , TreatmentAccess.as_view()),
    path('create-items-treatment/<name>/' , post_items_treatment),
    path('create-treatment/<name>/' ,post_treatment )
]