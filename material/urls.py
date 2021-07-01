from django.urls import path
from .views import *
urlpatterns=[
    path("new/", NewMaterial.as_view(), name="material-new"),
    path("view/", ViewMaterial.as_view(), name="material-view"),
    path("update/<int:pk>", UpdateMaterial.as_view(), name="material-update"),
    path("delete/<int:pk>", DeleteMaterial.as_view(), name="material-delete")
]