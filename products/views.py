from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import models
from django.db.utils import OperationalError


def staff_check(user):
    return user.is_staff


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
                models.Q(name__icontains=query) | models.Q(description__icontains=query)
            )

    except OperationalError:
        # Handles Heroku SQLite database reset safely
        products = []
        categories = []

    context = {
        "products": products,
        "categories": categories,
        "current_category": category_slug,
        "query": query,
    }
    return render(request, "products/product_list.html", context)


def product_detail(request, slug):
    try:
        product = get_object_or_404(Product, slug=slug, is_available=True)
    except OperationalError:
        product = None

    return render(
        request,
        "products/product_detail.html",
        {"product": product},
    )
