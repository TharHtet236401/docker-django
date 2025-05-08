from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render 
from .models import Book

def books(request):
    books = Book.objects.all()
    return render(request, 'booksManagement/books.html', {'books': books})


def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        response = render(request, 'booksManagement/book-detail.html', {'book': book})
        
        if not 'HX-Request' in request.headers:
            response['HX-Retarget'] = '#base-container'
            print(response)
            response['HX-Push-Url'] = f'/{pk}/'
            
        return response
    except Book.DoesNotExist:
        return HttpResponse("Book not found", status=404)

