from django.urls import path
from .views import *
urlpatterns=[
    path("new/", NewSupplier.as_view(), name="supplier-new"),
    path("view/", ViewSupplier.as_view(), name="supplier-view"),
    path("update/<int:pk>", UpdateSupplier.as_view(), name="supplier-update"),
    path("delete/<int:pk>", DeleteSupplier.as_view(), name="supplier-delete")

]