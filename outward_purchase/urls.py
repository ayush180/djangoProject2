from django.urls import path
from .views import *
urlpatterns=[
        path("new/", NewInwardBill.as_view(), name="purchase-new"),
        path("closed/", closewindow, name="close"),
        path("view/", ViewPurchaseBill.as_view(), name="purchase-view"),
        path("detail/<int:pk>", DetailPurchaseBill.as_view(), name="purchase-detail"),
        path("update/<int:pk>", UpdatePurchaseBill.as_view(), name="purchase-update"),
        path("delete/<int:pk>", DeletePurchaseBill.as_view(), name="purchase-delete")

]