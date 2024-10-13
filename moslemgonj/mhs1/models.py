from django.db import models

# Create your models here.

class Contact(models.Model):
    name= models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.TextField()
    disc=models.TextField()
    def __str__(self):
        return self.name    


    

 
   
