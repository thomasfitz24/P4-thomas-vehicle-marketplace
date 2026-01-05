import stripe

from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from products.models import Product


stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def create_checkout_session(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_available=True)

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "gbp",
                    "product_data": {
                        "name": product.name,
                    },
                    "unit_amount": int(product.price * 100),
                },
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url=request.build_absolute_uri(
            f"/checkout/success/?product_id={product.id}"
        ),
        cancel_url=request.build_absolute_uri("/checkout/cancel/"),
    )

    return redirect(checkout_session.url, code=303)


@login_required
def checkout_success(request):
    product_id = request.GET.get("product_id")

    if product_id:
        product = get_object_or_404(Product, id=product_id)
        product.is_available = False
        product.save()

    return render(request, "checkout/success.html")


@login_required
def checkout_cancel(request):
    return render(request, "checkout/cancel.html")
