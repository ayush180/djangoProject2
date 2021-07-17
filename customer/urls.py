from django.urls import path
from .views import *
urlpatterns=[
    path("new/", NewCustomer.as_view(), name="customer-new"),
    path("view/", ViewCustomer.as_view(), name="customer-view"),
    path("update/<int:pk>", UpdateCustomer.as_view(), name="customer-update"),
    path("delete/<int:pk>", DeleteCustomer.as_view(), name="customer-delete"),
    path("detail/<int:pk>", Detail.as_view(), name="customer-detail")

]