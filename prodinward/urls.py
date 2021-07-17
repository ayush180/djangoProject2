from django.urls import path
from .views import *
urlpatterns=[
    path("new/", Newproduct.as_view(), name="prodinward-new"),
    path("view/", Viewproduct.as_view(), name="prodinward-view"),
    path("update/<int:pk>", Updateproduct.as_view(), name="prodinward-update"),
    path("delete/<int:pk>", Deleteproduct.as_view(), name="prodinward-delete")
]