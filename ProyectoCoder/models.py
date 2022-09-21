from django.conf import settings
from django.db import models
from django.utils import timezone

class Post (models.Model):
    author =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.Charfield (max_length=50)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date =models.DateTimeField (
            blank =True, null =True)  
    
    def publish (self):
        self.published_date =timezone.now()
        self.save()

    def __str_ (self):
        return self.title    
