from django.db import models
import uuid
# Create your models here.


class Products(models.Model):
    id = models.UUIDField(primary_key=True,unique=True ,default=uuid.uuid4(),editable=False)
    title = models.CharField(max_length=150, blank=True,null=True)
    descreption = models.TextField(max_length=500,  blank=True, null=True)
    prise = models.DecimalField(max_digits=9, decimal_places=2, default=00.00,null=True, blank=True)
    img = models.ImageField(upload_to='static/images/',default='static/images/placeholder/img.png')
