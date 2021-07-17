from django.urls import path
from .views import *
urlpatterns=[
    path("new/", Newsubcategory.as_view(), name="subcategory-new"),
    path("view/", Viewsubcategory.as_view(), name="subcategory-view"),
    path("update/<int:pk>", Updatesubcategory.as_view(), name="subcategory-update"),
    path("delete/<int:pk>", Deletesubcategory.as_view(), name="subcategory-delete")
]