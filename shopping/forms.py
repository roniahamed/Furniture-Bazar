from django import forms
from shopping.models import BillingAddress,Order




class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['first_name','last_name','phone_number','email_address','address','address2','city','zipcode']

        widgets ={
            'first_name' : forms.TextInput(attrs={'class': 'form-control', 'id':'first'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control' , 'id':'last'}),
            'phone_number' : forms.TextInput(attrs={'class': 'form-control', 'id':'number'}),
            'email_address' : forms.TextInput(attrs={'class': 'form-control', 'id':'email'}),
            'address' : forms.TextInput(attrs={'class': 'form-control', 'id':'add1'}),
            'address2' : forms.TextInput(attrs={'class': 'form-control', 'id':'add2'}),
            'city' : forms.TextInput(attrs={'class': 'form-control', 'id':'city'}),
            'zipcode' : forms.TextInput(attrs={'class': 'form-control', 'id':'zip'}),
            
        }

        
        