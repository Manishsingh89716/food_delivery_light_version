from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view),
    path("booking/customer/<int:user_id>/", views.customer_dashboard),
    path("booking/customer/<int:user_id>/create/", views.create_booking),
    path("booking/delivery/<int:user_id>/", views.delivery_dashboard),
    path("booking/delivery/update_status/", views.update_status),
    path("booking/admin/<int:user_id>/", views.admin_dashboard),
    path("booking/admin/assign/", views.assign_booking),
]