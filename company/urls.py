from django.contrib import admin
from django.urls import path
from python_django import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.test_form),
    path('form/', views.program_form),
    path('credit/', views.credit_form),
    path('client/', views.client_form),
    path('search/', views.search),
    path('all_clients/', views.client_view),
    path('all_credits/', views.credit_view, name="all_credits"),

]
