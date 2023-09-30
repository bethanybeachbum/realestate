from django import forms


class AddressForm(forms.Form):
    address = forms.CharField(label="stree", max_length=100)
    address2 = forms.CharField(label="city state, zip", max_length=100)

#  COPY THIS:
class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
