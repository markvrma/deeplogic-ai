import uuid
from django.db import models
import os

# each file uploaded will have a unique name
def update_filename(instance, filename):
    return f'uploads/{instance.id}_{filename}'

# Create your models here.
# file model
class UploadedFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to=update_filename)
    uploaded_at = models.DateTimeField(auto_now_add=True)