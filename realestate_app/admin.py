from django.contrib import admin

# Register your models here.
# the dot in front of models tells Django to look for
# models.py in shte same directory as admin.py
from .models import Contract
from .models import ContractDetail
from .models import Action
from .models import Person

# this tells Django to manage our model through the admin site
admin.site.register(Contract)
admin.site.register(Action)
admin.site.register(Person)
admin.site.register(ContractDetail)
