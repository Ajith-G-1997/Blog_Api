from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class Item(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    file_upload = models.FileField(
        upload_to='item_files/',  # Change 'item_files/' to your desired upload path
        validators=[
            FileExtensionValidator(
                allowed_extensions=['pdf', 'jpg', 'jpeg', 'png', 'gif'],
                message="Invalid file format. Allowed formats are PDF, JPG, JPEG, PNG, GIF."
            ),
        ],
        error_messages={
            'max_size': "File size exceeds the limit of 10MB. Please upload a smaller file."
        }
    )
   

    


    def __str__(self):
        return self.item_name
