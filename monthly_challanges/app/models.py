from django.db import models

class Product:
    id = models.IntegerField((""))
    name =models.CharField((""), max_length=50)
    discription= models.TextField((""))
    image=models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
