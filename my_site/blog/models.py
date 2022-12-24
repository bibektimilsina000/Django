from django.db import models
from django.core.validators import MinLengthValidator


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.first_name +" " + self.first_name


class Posts(models.Model):

    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=50)
    imageName = models.CharField(max_length=50)
    slug = models.SlugField()
    date = models.DateField(auto_now=True, auto_now_add=False)
    content = models.TextField(validators=[MinLengthValidator(10)])

    def __str__(self):
        return self.title
