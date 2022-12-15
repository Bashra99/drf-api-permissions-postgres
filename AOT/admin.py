from django.contrib import admin

# Register your models here.
from .models import AOT
from .models import Titan

admin.site.register(AOT)
admin.site.register(Titan)
