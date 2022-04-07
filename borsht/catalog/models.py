from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('catalog:dish_list_by_category',
                        args=[self.slug])

class Dish(models.Model):
    """
    Model representing a dish.
    """
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the dish")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ManyToManyField(Category)
    cooking_time = models.TimeField(auto_now=False, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=0, default=0)
    address = models.CharField(max_length=500, null=True)
    img = models.ImageField(upload_to='dish', null=True, blank=True, default="default.png")


    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


    def get_absolute_url(self):
        """
        Returns the url to access a particular dish instance.
        """
        return reverse('book-detail', args=[str(self.id)])
