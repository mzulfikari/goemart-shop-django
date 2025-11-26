from django.urls import path
from .. import views


urlpatterns = [
    path("address/list/",views.CustomerSecurityEditView.as_view(),name="address-list"),
    path("address/create/",views.CustomerProfileEditView.as_view(),name="address-create"),
    path("address/<int:pk>/edit",views.CustomerProfileImageEditView.as_view(),name="address-edit"),
    path("address/<int:pk>/delete",views.CustomerProfileImageEditView.as_view(),name="address-delete"),
]