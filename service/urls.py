from django.urls import path

from . import views


urlpatterns = [
    path("", views.ServiceListCreateView.as_view()),
    path("<service_id>", views.ServiceRetrieveUpdateDestroyView.as_view()),

]