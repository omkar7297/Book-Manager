from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title

class Login(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.email
    

class Registration(models.Model):
    name = models.CharField(max_length=50)
    mobilenumber = models.CharField(max_length=12)
    email = models.EmailField(max_length=30)
    city = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email  # Returning just the email for representation
