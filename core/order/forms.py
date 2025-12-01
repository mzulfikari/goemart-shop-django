from django import forms
from order.models import UserAddressModel,CouponModel
from django.utils import timezone


class CheckOutForm(forms.Form):
    address_id = forms.IntegerField(required=True,error_messages={
            "required": "لطفا یک آدرس را انتخاب کنید",
            "invalid": "آدرس معتبر نیست"
            })
    
    coupon = forms.IntegerField(required=True)
    
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
    
    def clean_coupon(self):
        code =self.cleaned_data.get('coupon')
        coupon = None        
        user = self.request.user
        try :
            coupon = CouponModel.objects.get(code=code)
        except CouponModel.DoesNotExist:
            raise forms.ValidationError("کد تخفیف معتبر نیست")
        if coupon:
            if coupon.used_by.count() >= coupon.max_limit_usage:
                raise forms.ValidationError("حد استفاده از این کد تخفیف به پایان رسیده است")
            
            if coupon.expiration_date and coupon.expiration_date < timezone.now():
                raise forms.ValidationError("این کد تخفیف منقضی شده است")
            
            if user in coupon.used_by.all():
                raise forms.ValidationError("شما قبلا از این کد تخفیف استفاده کرده اید")
        return coupon