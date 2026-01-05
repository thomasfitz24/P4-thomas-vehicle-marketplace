from django.shortcuts import render, get_object_or_404
from django.db import OperationalError
from django.db.models import Q

from .models import Product, Category


def product_list(request):
    category_slug = request.GET.get("category")
    query = request.GET.get("q")

    try:
        products = Product.objects.filter(is_available=True)
        categories = Category.objects.all()

        if category_slug:
            products = products.filter(category__slug=category_slug)

        if query:
            products = products.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )

    except OperationalError:
        products = []
        categories = []

    context = {
        "products": products,
        "categories": categories,
        "current_category": category_slug,
        "query": query,
    }
    return render(request, "products/product_list.html", context)
