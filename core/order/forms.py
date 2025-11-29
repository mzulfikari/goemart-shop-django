from django import forms
from order.models import UserAddressModel


class CheckOutForm(forms.Form):
    address_id = forms.IntegerField(required=True,error_messages={
            "required": "لطفا یک آدرس را انتخاب کنید",
            "invalid": "آدرس معتبر نیست",
        }
    )
    
    def __init__(self,*args,**kwargs):
        self.request = kwargs.pop('request',None)
        super(CheckOutForm,self).__init__(*args, **kwargs)
        
    def clean_address_id(self):
        address_id = self.cleaned_data.get('address_id')
        user = self.request.user
        try :
            address = UserAddressModel.objects.get(id=address_id,user=user)
        except UserAddressModel.DoesNotExist:
            raise forms.ValidationError("لطفا یک آدرس را انتخاب کنید")
        return address