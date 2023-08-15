from django.db import models
import uuid

# Create your models here.

class Publisher(models.Model):
    """
    we want to have uniq id like: dwqd-1231-adawD-212
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    