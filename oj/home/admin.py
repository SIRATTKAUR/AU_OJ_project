from django.contrib import admin

# Register your models here.
from .models import Problems, test_cases

admin.site.register(Problems)

admin.site.register(test_cases)