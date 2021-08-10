from django.urls import path
from . import views

urlpatterns = [
    path('count/<int:angka>/', views.count),
    path('sapa/<str:nama>/', views.sapa),
    path('shop/', views.shop),
    path('shop/laptop/', views.shop_laptop),
    path('shop/smartphone/', views.shop_smartphone),
    path('shop/console/', views.shop_console),
    path('firstpage/', views.first_page),
    path('secondpage/', views.second_page),
    path('example/', views.example),
    path('profile/', views.profile),
    path('second/', views.second_page),
    path('', views.landing_page),
]
