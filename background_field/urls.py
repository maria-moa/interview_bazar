from django.urls import re_path

from . import views


urlpatterns = [
    re_path("^$", views.BackGroundFieldCreateView.as_view()),
    re_path(r"^mine$", views.RetrieveMyBackGroundFieldView.as_view()),
    re_path(r"(?P<background_field_id>[0-9]+)", views.BackGroundFieldRetrieveUpdateDestroyView.as_view()),
]
