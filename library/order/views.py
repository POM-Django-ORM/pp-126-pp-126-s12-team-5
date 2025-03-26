# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Order, Book
from .models import CustomUser
from django.views.decorators.csrf import csrf_exempt
import json

def order_list(request):
    orders = Order.objects.all()
    orders_data = [order.to_dict() for order in orders]
    return JsonResponse({'orders': orders_data})

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return JsonResponse(order.to_dict())

@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        book_id = data.get('book_id')
        plated_end_at = data.get('plated_end_at')

        user = get_object_or_404(CustomUser, id=user_id)
        book = get_object_or_404(Book, id=book_id)
        
        order = Order.objects.create(user=user, book=book, plated_end_at=plated_end_at)
        return JsonResponse(order.to_dict(), status=201)

    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def update_order(request, order_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        order = get_object_or_404(Order, id=order_id)

        plated_end_at = data.get('plated_end_at', order.plated_end_at)
        end_at = data.get('end_at', order.end_at)

        order.update(plated_end_at=plated_end_at, end_at=end_at)
        return JsonResponse(order.to_dict(), status=200)

    return JsonResponse({'error': 'Invalid method'}, status=405)
