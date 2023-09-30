from django.shortcuts import render, redirect
from realestate_app.models import Action, Contract, Person, ContractDetail
from .models import Contract, Action, Person,  ContractDetail
from .forms import ContractForm, ActionForm
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.views.generic import TemplateView
from django.template import loader

import requests
import pprint

# Create your views here.
""" When a URL request matches the pattern we just defined, Django looks for a function
called index() in view.py.  Django then passes the request object to this view function.
 """


def index(request):
  """The home page for realestate_app """
  # Generate counts for some of the main objects
  num_contracts = Contract.objects.all().count()
  num_actions = Action.objects.all().count()
  num_persons = Person.objects.all().count()
  # num_my_actions = Action.objects.all().filter(owner=request.user).count()

  context = {
    'num_contracts': num_contracts,
    'num_actions': num_actions,
    'num_persons': num_persons,
    # 'num_my_actions' : num_my_actions,
  }

  return render(request, 'realestate_app/index.html', context=context)


@login_required
def contracts(request):
  """Show all contracts that are not closed
    closedYesNo == No
    """
  contracts = Contract.objects.filter(owner=request.user).order_by('addDate')
  context = {'contracts': contracts}
  return render(request, 'realestate_app/contracts.html', context)


@login_required
def contract(request, contract_id):
  """ Show a single contract and all its ACTIONS   """
  # Make sure the toic belongs to the current user.
  contract = Contract.objects.get(id=contract_id)
  if contract.owner != request.user:
    raise Http404

  actions = contract.action_set.order_by('action')

  context = {'contract': contract, 'actions': actions}

  return render(request, 'realestate_app/contract.html', context, )


def contractlist(request):
  """List all contracts"""
  contractlist = Contract.objects.order_by('AddDate')
  context = {'contractlist': contractlist}
  return render(request, 'realestate_app/contractlist.html', context)


def actions(request):
  """Show all actions"""
  actions = Action.objects.order_by('action')
  context = {'actions': actions}
  return render(request, 'realestate_app/actions.html', context)


@login_required
def action(request, contractaction_id):
  """Show details for one action """
  action = Action.objects.order_by('action')
  context = {'action': action}
  return render(request, 'realestate_app/action/int:<id>.html')


def persons(request):
  """Show all persons involved in one contract """
  action = Person.objects.order_by('last_name')
  context = {'persons': persons}
  return render(request, 'realestate_app/persons.html')


def person(request, person_id):
  """Show all information on one person """
  action = Person.objects.order_by('last_name')
  context = {'person': person}
  return render(request, 'realestate_app/persons/int<id>.html')


@login_required
def new_contract(request):
  """Add a new contract"""
  if request.method != 'POST':
    # No data submitted; create a blank form.
    form = ContractForm()
  else:
    # POST data submitted; process data.
    form = ContractForm(data=request.POST)
    if form.is_valid():
      new_contract = form.save(commit=False)
      new_contract.owner = request.user
      new_contract.save()
      return redirect('realestate_app:contracts')

  # Display a blank or invalid form.
  context = {'form': form}
  return render(request, 'realestate_app/new_contract.html', context)




@login_required
def new_action(request, contract_id):
  """Add a new action for a particular contract"""
  contract = Contract.objects.get(id=contract_id)

  if request.method != 'POST':
    # No data submitted, create a blank form.
    form = ActionForm()
  else:
    # POST data submitted, process data.
    form = ActionForm(data=request.POST)
    if form.is_valid():
      new_action = form.save(commit=False)
      new_action.contract = contract  # contract_action?
      new_action.save()
      return redirect('realestate_app:contract', contract_id=contract_id)

  # Display a blank or invalid form.
  context = {'contract': contract,
             'form': form
             }
  return render(request, 'realestate_app/new_action.html', context)


"""
1. When the edit_action page receive a GET request, the edit_action() function
returns a form for editing the entry.
2. When the pages receives a POST request with revised action text, it saves the
modified text into the database.
"""

#########################################################
@login_required
def edit_action(request, action_id):
  """ Edit an existing action . """
  action = Action.objects.get(id=action_id)
  contract = action.contract
  # if action.owner != request.user:ee
  # raise Http404

  if request.method != 'POST':
    # Initial request; pre-fill form with the current entry.
    form = ActionForm(instance=action)
  else:
    # POST data submitted; process data.
    form = ActionForm(instance=action, data=request.POST)
    if form.is_valid():
      form.save()
      return redirect('realestate_app:contract', contract_id=contract.id)

  context = {'action': action, 'contract': contract, 'form': form}
  return render(request, 'realestate_app/edit_action.html', context)



def about(request):
  # return HttpResponse('<h2> About Real Deal </h2>')
  return render(request, 'realestate_app/about.html')

def contract_detail(request):
  # return HttpResponse('<h2> About Real Deal </h2>')
  return render(request, 'realestate_app/contract_detail.html')

def property_lookup(request):
  # """ Hits ATTOM database for information"""
   return render(request, 'realestate_app/property_lookup.html')

def attom_location(request):
  # returns data from ATTOM DB
  baseUrl = 'https://api.gateway.attomdata.com'
  apiEndpoint = '/propertyapi/v1.0.0/property/detail'

  headers = {
    'apikey': "46d45307ab513b944f5fd8ea08b26a6a"
  }

  params = {
    "address1": "39678 Stephanie Drive",
    "address2": "Bethany Beach, DE"
  }

  # Send request, headers and params are both dicts
  response = requests.get(url=f'{baseUrl}{apiEndpoint}', headers=headers, params=params)

  # Parse full response, returning a dict
  jsonResponse = response.json()

  # print(f'response code: {response.status_code}\n\n')
  # print('Full Response:')
  # pprint.pprint(jsonResponse)
  # print('\n\n\n')

  # print(f'County: {jsonResponse["property"][0]["address"]["country"]}')
  # context = {'country' : "USA"}
  country1 = {jsonResponse["property"][0]["address"]["country"]}
  context = {'country': country1}
  return render(request,'realestate_app/attom_location.html', context)

def first(request):
  # template = loader.get_template('first.html')
  return render(request, 'realestate_app/first.html')
  # return HttpResponse(template.render())

