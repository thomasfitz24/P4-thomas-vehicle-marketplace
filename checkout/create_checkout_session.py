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
