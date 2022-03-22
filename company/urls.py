from django.contrib import admin
from django.urls import path
from python_django import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.test_form),
    path('form/', views.program_form),
    path('client_form/', views.clients_form),
    path('credit/', views.credit_form),
    path('client/', views.client_form),
    path('search/', views.search),
    path('clients/', views.client_view, name="all_clients"),
    path('credits/', views.credit_view, name="all_credits"),
    path('clients/filter/', views.filter_clients),
    path('clients/<int:id>/', views.detail_view),
    path('clients/<int:id>/delete/', views.delete_client),
    path('credits/<int:id>/delete/', views.delete_credit),




]
