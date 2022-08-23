from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_number = models.IntegerField()
    customer_email  = models.EmailField()
    customer_password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.customer_name

    
