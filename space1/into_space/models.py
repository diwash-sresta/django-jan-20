from django.db import models

class Launch(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    pilot = models.CharField(max_length = 100)
    launched_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title