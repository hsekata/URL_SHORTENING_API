from django.db import models

# Create your models here.


class URL(models.Model):
    url = models.CharField(max_length=255)
    shortcode = models.CharField(max_length=255, unique=True)
    createdAt = models.TimeField(auto_now_add=True)
    updatedAt = models.TimeField(auto_now=True)
    accessCount = models.IntegerField(default=0)
    

    def increment_access_count(self):
        
        self.accessCount += 1
        self.save(update_fields=['accessCount'])