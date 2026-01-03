from django.shortcuts import render


def checkout_success(request):
    return render(request, "checkout/success.html")


def checkout_cancel(request):
    return render(request, "checkout/cancel.html")
