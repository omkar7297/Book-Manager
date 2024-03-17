from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book  # Correct import statement assuming 'views.py' is inside the 'books' app directory
from .forms import BookForm  # Correct import statement assuming 'views.py' is inside the 'books' app directory



class BookListView(ListView):
    model = Book  # Set the model to Book
    template_name = 'books/book_list.html'  # Set the template name
    context_object_name = 'books'  # Set the name of the context variable for the list of objects    

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_update.html'
    success_url = reverse_lazy('book_list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')


