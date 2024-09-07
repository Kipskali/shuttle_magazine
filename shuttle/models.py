from django.db import models

# Create your models here.

class event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cover_photo = models.ImageField(blank=False)
    def __str__(self):
        return self.title

class photo(models.Model):
    photo = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200, blank=True) 
    event = models.ForeignKey(event, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.event.title


    
