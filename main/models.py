import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    CATEGORY_CHOICES = [
        ('ball', 'Ball'),
        ('sock', 'Sock'),
        ('boots', 'Boots'),
        ('shinguard', 'Shinguard'),
        ('jersey', 'Jersey'),
        ('hat', 'Hat'),
        ('glove', 'Glove')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField()
    price = models.IntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
# employee: name (<255 char), age (bil bulat), persona(text)

class Employee(models.Model):
    name = models.CharField(max_length=255)
    age = models.BigIntegerField()
    persona = models.TextField()
