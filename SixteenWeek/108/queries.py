from datetime import timedelta

from django.db.models import Avg, Count, Q, Sum
from django.utils import timezone

from .models import Company, Product, Employee, Customer, Order


def young_employees(job: str):
    return Employee.objects.filter(age__lt=30, job=job)


def cheap_products():
    avg_price = Product.objects.aggregate(
        avg=Avg("price")
    )["avg"]

    return Product.objects.filter(
        price__lt=avg_price
    ).order_by("price").values_list("name", flat=True)


def products_sold_by_companies():
    return Company.objects.annotate(
        sold=Sum("product__sold")
    ).values_list("name", "sold")


def sum_of_income(start_date: str, end_date: str):
    return Order.objects.filter(
        time__gte=start_date,
        time__lte=end_date
    ).aggregate(
        total=Sum("price")
    )["total"]


def good_customers():
    one_month_ago = timezone.now() - timedelta(days=30)

    return Customer.objects.filter(
        level="G",
        order__time__gte=one_month_ago
    ).annotate(
        purchases=Count("order")
    ).filter(
        purchases__gt=10
    ).values_list("name", "phone")


def nonprofitable_companies():
    return Company.objects.annotate(
        count=Count(
            "product",
            filter=Q(product__sold__lt=100)
        )
    ).filter(
        count__gte=4
    ).values_list("name", flat=True)