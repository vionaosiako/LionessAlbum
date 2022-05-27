from django.contrib import admin

# Register your models here.
from .models import Category,Pictures,Location

admin.site.register(Category),
admin.site.register(Pictures),
admin.site.register(Location),
