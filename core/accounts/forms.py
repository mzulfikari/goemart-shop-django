from django.contrib.auth import forms as auth_forms
from django.core.exceptions import ValidationError


class AuthenticationForm(auth_forms.AuthenticationForm):
    """Login customize Forms"""
    
    def confirm_login_allowed(self, user):
        super(AuthenticationForm,self).confirm_login_allowed(user)
        
    # if not user.is_verified:
    #     raise ValidationError("اطلاعات وارد شده صحیح نمی باشد")