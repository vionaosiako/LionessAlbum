from django.shortcuts import render
from .models import Category, Location,Pictures

# Create your views here.

def gallery(request):
    locations = Location.objects.all()
    categories = Category.objects.all()
    photos = Pictures.objects.all()
    context = {'locations':locations, 'categories' : categories, 'photos':photos}
        
    return render(request, 'gallery.html',context)

def viewPhoto(request,pk):
    photo = Pictures.objects.get(id=pk)
    return render(request, 'viewPhoto.html', {'photo':photo})

def addPhoto(request):
    return render(request, 'addPhoto.html')