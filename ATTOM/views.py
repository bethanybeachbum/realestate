from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
# from python file in same directory called prop_detail_func.py
# import one specific function: get_prop_detail()
from .prop_detail_func import get_prop_detail
from .forms import AddressForm

# Create your views here.
def index(request):
  return render(request, 'attom/index.html')

def property_detail(request):
  """ The Presentation of Property Data from ATTOM Database """
  # function goes out to public database and retries information and
  # puts in a list called "parsed_list"
  parsed_list = get_prop_detail()

  # Abstract specific fields from list
  context = {
    'property': parsed_list,
    'property_identifier': parsed_list[0]["identifier"]["attomId"],
    'property_address': parsed_list[0]["address"]["oneLine"],
    'property_lot_size': parsed_list[0]["lot"]["lotsize1"],
    'property_yearbuilt': parsed_list[0]["summary"]["yearbuilt"],
    'property_propertyType': parsed_list[0]["summary"]["propertyType"],
  }
  return render(request, 'attom/property_detail.html', context)


def get_property(request):
  """Form for getting address for ATTOM database search"""
  # if this is a POST request we need to process the form data
  if request.method != 'POST':
    # No data submitted; create a blank form.
    # create a form instance and populate it with data from the request:
    form = AddressForm()
    # check whether it is valid:
  else:
    # POST data submitted; process data.
    form = AddressForm(data=request.POST)
    if form.is_valid():
      form.save()
      return redirect("attom:property_detail.html")

  #Display a blank or invalid form.
  context = {'form': form}
  return render(request, "attom/property_detail.html",  context)

