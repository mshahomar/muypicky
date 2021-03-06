from django.db import models
from django.conf import settings
from django.urls import reverse
from restaurants.models import RestaurantLocation


class Item(models.Model):
    # associations
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant = models.ForeignKey(RestaurantLocation)
    # item stuff
    name = models.CharField(max_length=120)
    contents = models.TextField(help_text='Separate each menu items by comma')
    excludes = models.TextField(blank=True, null=True, help_text='Separate each menu items by comma')
    public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-timestamp']       #Items.objects.all()

    def __str__(self):
        return self.name

    def get_contents(self):
        return self.contents.split(",")

    def get_excludes(self):
        return self.excludes.split(",")

    def get_absolute_url(self):
        return reverse('menus:menus_detail', kwargs={'pk': self.pk})
