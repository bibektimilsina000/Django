from django.db import models
 
class Movies(models.Model):
    title = models.CharField(max_length=100) 
    description=models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    

    

 
    def __str__(self):
        return self.title

