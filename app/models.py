from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=11)
    company=models.CharField(max_length=40)
    service=models.CharField(max_length=50)
    detail=models.TextField()

    def __str__(self):
        return self.name + " " + self.phone