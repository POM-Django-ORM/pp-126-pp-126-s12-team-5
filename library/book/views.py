# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
import json

def book_list(request):
    books = Book.objects.all()
    books_data = [book.to_dict() for book in books]
    return JsonResponse({'books': books_data})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return JsonResponse(book.to_dict())

@csrf_exempt
def create_book(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        description = data.get('description')
        count = data.get('count', 10)
        authors = data.get('authors', [])
        
        book = Book.objects.create(name=name, description=description, count=count)
        return JsonResponse(book.to_dict(), status=201)
    return JsonResponse({'error': 'Invalid method'}, status=405)
