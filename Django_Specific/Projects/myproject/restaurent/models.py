from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=300)
    address1 = models.CharField(max_length=150, blank=True)
    address2 = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.CharField(max_length=80)
    review = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
