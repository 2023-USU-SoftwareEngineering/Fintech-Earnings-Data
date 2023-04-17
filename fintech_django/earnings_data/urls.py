from django.urls import path

from . import views

app_name = 'earnings_data'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('search/', views.search, name='search'),
]