from django.test import TestCase
from .models import Pictures,Category,Location


# Create your tests here.

class CategoryTestClass(TestCase):
    def setUp(self):
        self.rare = Category(name="Boooks")

    def test_save_category(self):
        self.rare.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)


