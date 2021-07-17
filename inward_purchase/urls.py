from django.urls import path
from .views import *
urlpatterns=[
        path("new/", NewInwardBill.as_view(), name="new-purchase"),
        path("closed/", closewindow, name="closed"),
        path("view/", ViewPurchaseBill.as_view(), name="view-purchase"),
        path("update/<int:pk>", UpdatePurchaseBill.as_view(), name="update-purchase"),
        path("delete/<int:pk>", DeletePurchaseBill.as_view(), name="delete-purchase"),
        path("detail/<int:pk>", DetailPurchaseBill.as_view(), name="detail-purchase")
]