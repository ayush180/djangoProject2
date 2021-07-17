from django.urls import path
from .views import *
urlpatterns=[
    path("new/", NewLoss.as_view(), name="loss-new"),
    path("view/", ViewLoss.as_view(), name="loss-view"),
    path("update/<int:pk>", UpdateLoss.as_view(), name="loss-update"),
    path("delete/<int:pk>", DeleteLoss.as_view(), name="loss-delete")
]