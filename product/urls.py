from django.urls import path
from .views import *
urlpatterns=[
    path("new/", Newproduct.as_view(), name="product-new"),
    path("view/", Viewproduct.as_view(), name="product-view"),
    path("update/<int:pk>", Updateproduct.as_view(), name="product-update"),
    path("delete/<int:pk>", Deleteproduct.as_view(), name="product-delete"),
    path("detail/<int:pk>", Detail.as_view(), name="product-detail")
]