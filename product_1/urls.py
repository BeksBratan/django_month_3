from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.HomePageView.as_view(), name='home_page_url'),
    path('product/<int:id>/', views.HomePageDetailView.as_view(), name='home_page_detail_view'),
    path('add/', views.HomePageCreateView.as_view(), name='add_home_page.view'),
    path('add-customer/', views.HomePageCreateView2.as_view(), name='add_customer.view'),

]