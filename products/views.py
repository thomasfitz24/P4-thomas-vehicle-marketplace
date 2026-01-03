from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.contrib.auth.decorators import login_required, user_passes_test


def staff_check(user):
    return user.is_staff

def product_list(request):
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.all()

    category_slug = request.GET.get("category")
    if category_slug:
        products = products.filter(category__slug=category_slug)

    context = {
        "products": products,
        "categories": categories,
        "current_category": category_slug,
    }
    return render(request, "products/product_list.html", context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)
    return render(request, "products/product_detail.html", {"product": product})
