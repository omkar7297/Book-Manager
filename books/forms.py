from django import forms
from .models import Book, Login, Registration

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'published_date']
        
    def clean(self):
        cleaned_data = super().clean()
        # Add validation rules here
        title = cleaned_data.get('title')
        author = cleaned_data.get('author')
        genre = cleaned_data.get('genre')
        published_date = cleaned_data.get('published_date')
        if not title:
            self.add_error('title', 'Title is required.')
        if not author:
            self.add_error('author', 'Author is required.')
        if not genre:
            self.add_error('genre', 'Genre is required.')
        if not published_date:
            self.add_error('published_date', 'Published date is required.')
        return cleaned_data
        
class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['email', 'password']

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'mobilenumber', 'email', 'city', 'password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if Registration.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already registered.")
        return email    