from django.urls import path

from . import views


urlpatterns = [
    path("", views.WholeSaleListCreateView.as_view()),
    path("<wholeSale_id>", views.WholeSaleRetrieveUpdateDestroyView.as_view()),
]
