from django.shortcuts import render
from django.views.generic import( 
    FormView,
    TemplateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasCustomerAccessPermission
from order.models import UserAddressModel
from cart.models import CartModel
from .forms import CheckOutForm
from django.urls import reverse_lazy


class OrderCheckOutView(LoginRequiredMixin,HasCustomerAccessPermission,FormView):
    
    template_name = 'order/checkout.html'
    form_class = CheckOutForm
    success_url = reverse_lazy('order:completed')
    
    def get_form_kwargs(self):
        kwargs = super(OrderCheckOutView,self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    
    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        address = cleaned_data['address_id']
        print(address)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print(self.request.POST)
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = CartModel.objects.get(user=self.request.user)
        context['addresses'] = UserAddressModel.objects.filter(user=self.request.user)
        total_price = cart.calculate_total_price()
        context ['total_price'] = total_price
        context["total_max"] = int(total_price * 0.09)
        return context
    
class OrderCompletedOutView(LoginRequiredMixin,HasCustomerAccessPermission,FormView):
    
    template_name = 'order/order-completed.html.html'