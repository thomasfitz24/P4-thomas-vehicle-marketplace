import stripe
from django.conf import settings
from django.shortcuts import redirect, render
from products.models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_checkout_session(request, product_id):
    product = Product.objects.get(id=product_id)

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
        success_url=request.build_absolute_uri("/checkout/success/"),
        cancel_url=request.build_absolute_uri("/checkout/cancel/"),
    )

    return redirect(checkout_session.url, code=303)


def checkout_success(request):
    return render(request, "checkout/success.html")


def checkout_cancel(request):
    return render(request, "checkout/cancel.html")
