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

class OrderCheckOutView(LoginRequiredMixin,HasCustomerAccessPermission,FormView):
    
    template_name = 'order/checkout.html'
    form_class = CheckOutForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = CartModel.objects.get(user=self.request.user)
        context['addresses'] = UserAddressModel.objects.filter(user=self.request.user)
        total_price = cart.calculate_total_price()
        context ['total_price'] = total_price
        context["total_max"] = int(total_price * 0.09)
        return context