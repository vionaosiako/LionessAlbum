from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt


# Category
class Category(models.Model):
    
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls,id,name):
        cls.objects.filter(id = id).update(name = name)

    @classmethod
    def display_all_categories(cls):
        return cls.objects.all()
    
    # Pictures
class Pictures(models.Model):
    image = CloudinaryField('image')
    # image = models.ImageField(null=False, blank = False)
    name = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(max_length=1000)
    category = models.ForeignKey('Category',on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey('Location',on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_all_pictures(cls):
        pictures = Pictures.objects.all()
        return pictures

    @classmethod
    def get_pic_by_id(cls,id):
        pic = cls.objects.get(id=id)
        return pic

    @classmethod
    def search_by_category(cls,search_term):
        image = cls.objects.filter(category__name__icontains=search_term)
        return image

    @classmethod
    def filter_by_location(cls, location):
        pictures = Pictures.objects.filter(location__name=location)
        return pictures

    @classmethod
    def display_all_images(cls):
            return cls.objects.all()

    def save_picture(self):
        self.save()

    def update_picture(self,name,description,category):
        self.name = name,
        self.description = description,
        self.category = category
        self.save()

    def get_picture_by_id(cls,id):
        pic = Pictures.objects.get(id=id)
        return pic


    class Meta:
        ordering = ['-date']
        
# Location
class Location(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location
        
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls,id,name):
        cls.objects.filter(id = id).update(location = name)

    @classmethod
    def display_all_locations(cls):
        return cls.objects.all()
