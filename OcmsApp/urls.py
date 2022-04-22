from django.urls import path
from OcmsApp import views
from OcmsApp.models import Accounts

urlpatterns = [
    path('account', views.AccountApi),
    path('account/<int:id>', views.AccountApi)
]