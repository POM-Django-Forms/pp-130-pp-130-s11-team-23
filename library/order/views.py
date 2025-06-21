from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from order.models import Order
from book.models import Book
from django.utils.timezone import make_aware
from datetime import datetime
from django.http import HttpResponseForbidden
from .forms import OrderForm
from .forms import CloseOrderForm

@login_required
def order_list_view(request):
    if request.user.role != 1:
        return HttpResponseForbidden("Лише для адміністратора")
    orders = Order.objects.select_related('book', 'user').all()
    return render(request, 'order/order_list.html', {'orders': orders})

@login_required
def my_orders_view(request):
    orders = Order.objects.filter(user=request.user).select_related('book')
    return render(request, 'order/my_orders.html', {'orders': orders})

@login_required
def create_order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data['book']
            plated_end_at = form.cleaned_data['plated_end_at']

            order = Order.create(user=request.user, book=book, plated_end_at=plated_end_at)
            if order is None:
                return render(request, 'order/create_order.html', {
                    'form': form,
                    'error': 'Книгу вже замовлено.'
                })
            return redirect('my_orders')
    else:
        form = OrderForm()

    return render(request, 'order/create_order.html', {'form': form})

@login_required
def close_order_view(request, order_id):
    if request.user.role != 1:
        return HttpResponseForbidden("Лише для адміністратора")

    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        form = CloseOrderForm(request.POST)
        if form.is_valid():
            order.end_at = make_aware(datetime.combine(form.cleaned_data['end_at'], datetime.min.time()))
            order.save()
            return redirect('order_list')
    else:
        form = CloseOrderForm(initial={'end_at': datetime.today()})

    return render(request, 'order/close_order.html', {
        'form': form,
        'order': order
    })