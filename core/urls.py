from django.urls import path
from . import views

urlpatterns = [
    path('banks/', views.BankListAPIView.as_view(), name='bank-list'),
    path('branches/', views.BranchDetailAPIView.as_view(), name='branch-detail'),
    path('', views.home, name='home'),
]