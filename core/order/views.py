from django.shortcuts import render
from django.views.generic import( 
    FormView,
    TemplateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from decimal import Decimal
from dashboard.permissions import HasCustomerAccessPermission
from order.models import OrderModel, UserAddressModel
from order.models import OrderModel,OrderItemModel
from .forms import CheckOutForm
from django.urls import reverse_lazy
from cart.cart import CartSession
from cart.models import CartModel



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
        cart = CartModel.objects.get(user=self.request.user)
        cart_items = cart.cart_items.all()
        order = OrderModel.objects.create(
            user = self.request.user,
            # order address information
            address = address.address,
            state = address.state,
            city = address.city,
            zip_code = address.zip_code,
            )
        for item in cart_items:
            OrderItemModel.objects.create(
                order = order,
                product = item.product,
                quantity = item.quantity,
                price = item.product.get_price()
                )
        cart_items.delete()
        CartSession(self.request.session).clear()
        total_price = order.calculate_total_price
        if coupon:
            total_price = total_price - round((total_price * Decimal(coupon.discount_percent / 100)))
            order.coupon = coupon
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
    
class OrderCompletedOutView(LoginRequiredMixin,HasCustomerAccessPermission,TemplateView):
    
    template_name = 'order/order-completed.html'