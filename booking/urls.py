from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('about/',views.about, name='about'), #about page
    path('new-form/', views.book_demo, name='book_demo'),
    path('thank_you/', views.thank_you, name='thank_you'),
]