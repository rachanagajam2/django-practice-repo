from django.db import models
import uuid
# Create your models here.
class order_details(models.Model):
    useremail=models.EmailField(unique=True)
    order_id=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    mode=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    dateandtime=models.DateTimeField(default="INR")
    transcation_id=models.DateTimeField()
class MovieBooking(models.Model):
    moviename=models.CharField(max_length=50)