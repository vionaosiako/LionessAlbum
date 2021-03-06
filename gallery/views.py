from django.shortcuts import render
from .models import Category, Location,Pictures

# Create your views here.

def gallery(request):
    locations = Location.objects.all()
    categories = Category.objects.all()
    photos = Pictures.objects.all()
    context = {'locations':locations, 'categories' : categories, 'photos':photos}
    
    return render(request, 'gallery.html',context)

def search_results(request):

    if 'pictures' in request.GET and request.GET["pictures"]:
        search_term = request.GET.get("pictures")
        searched_pictures = Pictures.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"pictures": searched_pictures})
    else:
        message = "You haven't searched for any category"
        return render(request, 'all_art/search.html',{"message":message})

def viewPhoto(request,pk):
    photo = Pictures.objects.get(id=pk)
    return render(request, 'viewPhoto.html', {'photo':photo})

def addPhoto(request):
    return render(request, 'addPhoto.html')