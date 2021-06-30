from django.urls import  path
from .views import *

urlpatterns=[
    path("new/",NewCategory.as_view(),name="category-new"),
    path("view/",ViewCategory.as_view(),name="category-view"),
    path("update/<int:pk>",UpdateCategory.as_view(),name="category-update"),
    path("delete/<int:pk>",DeleteCategory.as_view(),name="category-delete")
]