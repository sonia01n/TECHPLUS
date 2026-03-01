from django.db import models

class Tool(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    is_trending = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']