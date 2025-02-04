from django.db import models
from author.models import Author

class Post(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    ]
    title = models.CharField(max_length = 100)
    content = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
    )
    # author = models.CharField(max_length = 100)
    published_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    

    def __str__(self):
        return (f"{self.title},{self.content},{self.author}")
        
    