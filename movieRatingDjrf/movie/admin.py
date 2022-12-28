from django.contrib import admin
from .models import Movies

@admin.register(Movies)
class Admin(admin.ModelAdmin):
    pass

