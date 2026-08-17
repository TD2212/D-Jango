from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("users/", views.users, name="users"),
    path("products/", views.products, name="products"),
    path("orders/", views.orders, name="orders"),
    path("reports/", views.reports, name="reports"),
    path("settings/", views.settings, name="settings"),
    path("profile/", views.profile, name="profile"),
]