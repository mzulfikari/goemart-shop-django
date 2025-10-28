from django import template
from shop.models import ProductStatusType,ProductModel

register = template.Library()


@register.inclusion_tag('includes/latest-product.html')
def show_latest_product():
    latest_product = ProductModel.objects.filter(
        status=ProductStatusType.publish.value).order_by("-created_date")[:8]
    return {"latest_products":latest_product}