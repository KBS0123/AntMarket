from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from decimal import Decimal


from orders.models import Order

def payment_process(request):
    order_id = request.session.get('order_id', None)
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        #결제 로직 추가
        Payment.objects.create(

        )

        return render(request, 'payment/process.html', locals())

    else:
        context = {'order_id': order_id}
        return render(request, 'payment/process.html', locals())

def payment_completed(request):

    return render(request, 'payment/completed.html')

def payment_canceled(request):
    return render(request, 'payment/canceled.html')
