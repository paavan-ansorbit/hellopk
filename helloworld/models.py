from django.db import models
from django.http import  JsonResponse
import json

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100 , unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return json.dumps({"name": self.name, "email": self.email, "address": self.address, "phone": self.phone, "created_at": self.created_at, "updated_at": self.updated_at})