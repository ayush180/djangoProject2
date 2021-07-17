from django.urls import path
from .views import *
urlpatterns=[
    path("new/", Newproduct.as_view(), name="prodoutward-new"),
    path("view/", Viewproduct.as_view(), name="prodoutward-view"),
    path("update/<int:pk>", Updateproduct.as_view(), name="prodoutward-update"),
    path("delete/<int:pk>", Deleteproduct.as_view(), name="prodoutward-delete")
]