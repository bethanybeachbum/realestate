from django.urls import path, include
from . import views

app_name = 'attom'
urlpatterns = [
  #home page
  path('', views.index, name='index'),
  path('property_detail/', views.property_detail, name='property_detail.html'),

  # Include default auth urls.
  path('', include('django.contrib.auth.urls')),


]
