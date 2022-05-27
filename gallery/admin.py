from django.contrib import admin

# Register your models here.
from .models import *

admin.site.Register(Category),
admin.site.Register(Image)
admin.site.Register(Location)
