# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Author
import json

@csrf_exempt
def create_author(request):
    """
    Create a new author.
    :param request: HTTP request containing author data (name, surname, patronymic)
    :return: JsonResponse with the created author data
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        surname = data.get('surname')
        patronymic = data.get('patronymic')

        if not name or not surname or not patronymic:
            return JsonResponse({'error': 'Missing fields'}, status=400)

        author = Author.create(name, surname, patronymic)
        return JsonResponse(author.to_dict(), status=201)

@csrf_exempt
def get_author_by_id(request, author_id):
    """
    Get author details by ID.
    :param author_id: ID of the author to retrieve
    :return: JsonResponse with author data or error if not found
    """
    if request.method == 'GET':
        author = Author.get_by_id(author_id)
        if author:
            return JsonResponse(author.to_dict(), status=200)
        else:
            return JsonResponse({'error': 'Author not found'}, status=404)

@csrf_exempt
def update_author(request, author_id):
    """
    Update an existing author's details.
    :param request: HTTP request containing updated author data
    :param author_id: ID of the author to update
    :return: JsonResponse with updated author data
    """
    if request.method == 'PUT':
        data = json.loads(request.body)
        author = Author.get_by_id(author_id)
        if not author:
            return JsonResponse({'error': 'Author not found'}, status=404)

        name = data.get('name')
        surname = data.get('surname')
        patronymic = data.get('patronymic')

        author.update(name, surname, patronymic)
        return JsonResponse(author.to_dict(), status=200)

@csrf_exempt
def delete_author(request, author_id):
    """
    Delete an author by ID.
    :param author_id: ID of the author to delete
    :return: JsonResponse indicating success or failure
    """
    if request.method == 'DELETE':
        success = Author.delete_by_id(author_id)
        if success:
            return JsonResponse({'message': 'Author deleted successfully'}, status=200)
        else:
            return JsonResponse({'error': 'Author not found'}, status=404)

@csrf_exempt
def get_all_authors(request):
    """
    Get all authors.
    :return: JsonResponse with list of all authors
    """
    if request.method == 'GET':
        authors = Author.get_all()
        authors_list = [author.to_dict() for author in authors]
        return JsonResponse(authors_list, safe=False, status=200)
