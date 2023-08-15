from django.db import models

# Create your models here.

class Author(models.Model):
    """
    Book author class
    Managed only in django admin
    """
    name = models.CharField(max_length=200)
    
    def _str_(self):
        return f"Author: {self.name}"