from django.urls import path
from . import views

urlpatterns = [
    path('', views.shelfs, name='shelfs'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('contact/', views.contact, name='contact'),
    path('favourites/', views.favourites, name='favourites'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('quote/', views.quote, name='quote'),
    path('rate/', views.rate, name='rate'),
    path('addToFvrt/', views.addToFvrt, name='addToFvrt')
]
