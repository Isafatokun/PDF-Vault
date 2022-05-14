from django.http import HttpResponse
from django.shortcuts import redirect, render


# Create your views here.
from .forms import OurForm
from .models import Book
from django.db.models import Q

def upload_book(request):
    if request.method == "POST":
        form = OurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("main:books")
    else:
        form = OurForm()

    return render(request, "main/upload.html", {"form" : form})


def show_books(request):
    query = " "
    if request.GET:
        query = request.GET['q']

    # Giving results based on saerch
    books = search_book(str(query))

    # Giving all results
    #books = Book.objects.all()
    
    return render(request, "main/books.html", {"books" : books} )


def search_book(query = None):
    queries_list = []
    queries = query.split(" ")
    for q in queries:
        books = Book.objects.filter(Q(title__icontains=q) | 
            Q(author_name__icontains=q)
        )

        for book in books:
            queries_list.append(book)
    return list(set(queries_list))