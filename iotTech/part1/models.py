from django.db import models
from django.utils.timezone import now

# Create your models here.
def user_directory_path(instance, filename):
    instance.name=filename
    return '{0}/{1}'.format(instance.userid, filename)



class Document(models.Model):
    userid=models.CharField(max_length=255, blank=True,default="")
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=255, blank=True,default="sss")