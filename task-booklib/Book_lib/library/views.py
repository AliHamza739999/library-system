from django.shortcuts import render , redirect
from django.db.models import Count, Avg, Max, Min
from .models import *
from .forms import *


def home(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    
    context = {'authors': authors, 'books': books , }
    return render(request, 'home.html', context)



def create_authorform(request):
    authorform = AuthorForm
    
    if request.method == 'POST':
        authorform = AuthorForm(request.POST)
        if authorform.is_valid():
            authorform.save()
            return redirect('home')
    
    context = {"authorform" :authorform ,}
    return render(request, 'authorform.html', context)


def author_details(request , pk):
    author = Author.objects.get(id=pk)
    
    context = {'author': author , }
    return render(request, 'author_details.html', context)


def author_update(request, pk):
    modell = Author.objects.get(id=pk)
    authorform = AuthorForm(instance=modell)
    
    if request.method == 'POST':
        authorform = AuthorForm(request.POST, instance=modell)
        if authorform.is_valid():
            authorform.save()
            return redirect('home')
           
    context = {"authorform" :authorform ,}
    return render(request, 'authorform.html', context)


def delete_author(request , pk):
    modell = Author.objects.get(id=pk)
    
    if request.method == 'POST' :
        modell.delete()
        return redirect('home')
    
    context = {'author' : modell ,}
    return render(request , 'author_delete.html' , context)


def create_bookform(request):
    bookforms = BookForm
    
    if request.method == 'POST':
        bookforms = BookForm(request.POST)
        if bookforms.is_valid():
            bookforms.save()
            return redirect('home')
    
    context = {"bookform" :bookforms ,}
    return render(request, 'bookform.html', context)


def book_details(request , pk):
    books = Book.objects.get(id=pk)
    
    context = {'book': books , }
    return render(request, 'book_details.html', context)



def update_bookform(request, pk):
    modell = Book.objects.get(id=pk)
    bookforms = BookForm(instance=modell)
    
    if request.method == 'POST':
        bookforms = BookForm(request.POST, instance=modell)
        if bookforms.is_valid():
            bookforms.save()
            return redirect('home')
           
    context = {"bookform" :bookforms ,}
    return render(request, 'bookform.html', context)



def delete_bookform(request , pk):
    modell = Book.objects.get(id=pk)
    
    if request.method == 'POST' :
        modell.delete()
        return redirect('home')
    
    context = {'book' : modell ,}
    return render(request , 'delete_book.html' , context)


def aggregation(request):
    aggregation = Book.objects.aggregate(
        total_books=Count('id'),
        average_price=Avg('price'),
        oldest_book=Min('publication_year'),
        newest_book=Max('publication_year'),
    )
    
    bookeachyear = Book.objects.values('publication_year').annotate(
        count=Count('id'))
    
    context = {'aggregation' : aggregation  , "bookeachyear" : bookeachyear}
    return render(request , 'aggregation.html' , context  )

