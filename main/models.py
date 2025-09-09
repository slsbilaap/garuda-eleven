from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('ball', 'Ball'),
        ('sock', 'Sock'),
        ('boots', 'Boots'),
        ('shinguard', 'Shinguard'),
        ('jersey', 'Jersey'),
        ('hat', 'Hat'),
        ('glove', 'Glove')
    ]

    name = models.CharField()
    price = models.IntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
