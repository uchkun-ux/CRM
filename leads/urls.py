from django.urls import path
from .views import *

app_name = "leads"

urlpatterns = [
    path('', leads_lists),
    path('<int:pk>/', lead_detail, name='detallar'),
    path('<int:pk>/update', lead_update, name="update"),
    path('<int:pk>/delete', lead_delete, name="lead-delete"),
    path('create-leads/', lead_create, name="lead-create")

]