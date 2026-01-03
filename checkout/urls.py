from django.urls import path
from . import views

app_name = "checkout"

urlpatterns = [
    path("buy/<int:product_id>/", views.create_checkout_session, name="buy"),
    path("success/", views.checkout_success, name="success"),
    path("cancel/", views.checkout_cancel, name="cancel"),
]
