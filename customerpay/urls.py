from django.urls import path
from .views import *
urlpatterns=[
    path("new/",NewPayment.as_view(), name="customerpay-new"),
    path("view/", ViewPayment.as_view(), name="customerpay-view"),
    path("update/<int:pk>", UpdatePayment.as_view(), name="customerpay-update"),
    path("delete/<int:pk>", DeletePayment.as_view(), name="customerpay-delete")
]