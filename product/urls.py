from django.urls import path

from . import views


urlpatterns = [
    path("", views.ProductListCreateView.as_view()),
    path("<product_id>", views.ProductRetrieveUpdateDestroyView.as_view()),
]
