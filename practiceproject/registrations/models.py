from django.db import models
import uuid

# Create your models here.
class CourseRegistration(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    course=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    registered_at=models.DateTimeField(auto_now_add=True)



class MovieBooking(models.Model):
    moviename = models.CharField(max_length=100)
    showtime = models.CharField(max_length=100)
    screenname = models.CharField(max_length=100)
    dateandtime = models.DateTimeField(auto_now_add=True)
    transaction_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
class MovieBooking1(models.Model):
    moviename = models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    showtime = models.CharField(max_length=100)
    screenname = models.CharField(max_length=100)
    dateandtime = models.DateTimeField(auto_now_add=True)
    transaction_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )