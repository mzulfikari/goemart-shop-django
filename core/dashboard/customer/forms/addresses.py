from django import forms
from order.models import UserAddressModel

class UserAddressForm(forms.Form):
    
    class Meta:
        model = UserAddressModel
        fields = [
            "address",
            "state",
            "city",
            "zip_code",
        ]