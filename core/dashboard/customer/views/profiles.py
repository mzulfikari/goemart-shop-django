from django.views.generic import View,UpdateView
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasCustomerAccessPermission
from django.contrib.auth import views as auth_views
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from dashboard.admin.forms import AdminPasswordChangeForm,AdminProfileEditForm
from accounts.models import Profile
from django.contrib import messages


class CustomerSecurityEditView(LoginRequiredMixin,HasCustomerAccessPermission,auth_views.PasswordChangeView,SuccessMessageMixin):
    
    template_name = 'dashboard/customer/profile/security-edit.html'
    form_class = AdminPasswordChangeForm
    success_url = reverse_lazy('dashboard:customer:security-edit')
    success_message = "بروز رسانی با موفقیت انجام شد "
    
    
class CustomerProfileEditView(LoginRequiredMixin,HasCustomerAccessPermission,UpdateView,SuccessMessageMixin):
    
    template_name = 'dashboard/customer/profile/profile-edit.html'
    form_class = AdminProfileEditForm
    success_url = reverse_lazy('dashboard:customer:profile-edit')
    success_message = "بروز رسانی پروفایل با موفقیت انجام شد "
    
    def get_object(self,queryset =None):
        return Profile.objects.get(user=self.request.user)
    

class CustomerProfileImageEditView(LoginRequiredMixin,HasCustomerAccessPermission,UpdateView,SuccessMessageMixin):
    
    http_method_names= ["post"]
    model = Profile
    fields = [
        "image"
    ]
    success_url = reverse_lazy('dashboard:customer:profile-edit')
    success_message = "بروز رسانی پروفایل با موفقیت انجام شد "
    
    def get_object(self,queryset =None):
        return Profile.objects.get(user=self.request.user)
    
    def form_invalid(self, form):
        messages.error(self.request,"ارسال تصویر با مشکل مواجه شده لطفا مجدد بررسی و تلاش نماید")
        return redirect(self.success_url)
