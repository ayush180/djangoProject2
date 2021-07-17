from django.urls import path
from .views import *
urlpatterns=[
    path("new/", NewEmployee.as_view(), name="employee-new"),
    path("view/", ViewEmployee.as_view(), name="employee-view"),
    path("update/<int:pk>", UpdateEmployee.as_view(), name="employee-update"),
    path("delete/<int:pk>", DeleteEmployee.as_view(), name="employee-delete"),
    path("detail/<int:pk>", Detail.as_view(), name="employee-detail")

]