from django.shortcuts import render, get_object_or_404
from django.db import models
from .models import Product, Category


def product_list(request):
    category_slug = request.GET.get("category")
    query = request.GET.get("q")

    products = Product.objects.filter(is_available=True)
    categories = Category.objects.all()

    if category_slug:
        products = products.filter(category__slug=category_slug)

    if query:
        products = products.filter(
            models.Q(name__icontains=query) | models.Q(description__icontains=query)
        )

    context = {
        "products": products,
        "categories": categories,
        "current_category": category_slug,
        "query": query,
    }
    return render(request, "products/product_list.html", context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)
    return render(
        request,
        "products/product_detail.html",
        {"product": product},
    )
