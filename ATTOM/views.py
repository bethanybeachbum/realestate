from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'attom/index.html')

def property_detail(request):
  return render(request, 'attom/property_detail.html')

