from django.urls import path,re_path
from . import views

app_name = 'shop'

urlpatterns = [
    path('product/grid/',views.ShopProductGrid.as_view(),name="product-grid"),
    re_path(r'^product/(?P<slug>[-\w\u0600-\u06FF]+)/detail/$',views.ShopProductDetailView.as_view(),name='product-detail')

]
