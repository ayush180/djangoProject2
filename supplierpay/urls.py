from django.urls import path
from .views import *
urlpatterns=[
    path("new/",NewPayment.as_view(), name="supplierpay-new"),
    path("view/", ViewPayment.as_view(), name="supplierpay-view"),
    path("update/<int:pk>", UpdatePayment.as_view(), name="supplierpay-update"),
    path("delete/<int:pk>", DeletePayment.as_view(), name="supplierpay-delete")
]