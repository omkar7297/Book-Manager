from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.db import connection
from .models import Book
from .forms import BookForm, LoginForm, RegistrationForm

class BookLogin(FormView):
    template_name = 'books/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        
        # Authenticate user against the books_login table
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM books_registration WHERE email = %s AND password = %s", [email, password])
            user = cursor.fetchone()

        if user is not None:
            print("Successful login")
            # Perform any additional logic if needed
            return HttpResponseRedirect(reverse_lazy('book_add'))
        else:
            print("Failed login")
            form.add_error(None, 'Invalid email or password')
            return render(self.request, self.template_name, {'form': form})

class BookRegistration(FormView):
    template_name = 'books/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('book_list')  # Redirect to book list after successful registration

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'book_list'

class BookAddView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_add.html'
    success_url = reverse_lazy('book_list')  # Redirect to book list after successful addition

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_update.html'
    success_url = reverse_lazy('book_list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')
