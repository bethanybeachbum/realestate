from django.urls import path, include
from . import views

#
# If you want to make your own custom paths,
# the first parameter is the URL (such as example.com/**admin**),
# the second parameter is the function to call to produce the web page,
# the third is just a name for the path.
#

app_name = 'attom'
urlpatterns = [
  #home page
  path('', views.index, name='index'),

  path('property_detail/', views.property_detail, name='property_detail.html'),

  # Include default auth urls.
  path('', include('django.contrib.auth.urls')),

  # path for looking up property detail
  # this URL sends rquests to the view function get_property()
  path('property_lookup/', views.get_property, name='get_property'),



]
