from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
import uuid
# Create your models here.


class Products(models.Model):
    id = models.UUIDField(primary_key=True, unique=True,
                          default=uuid.uuid4(), editable=False)
    title = models.CharField(max_length=150, blank=True, null=True)
    descreption = models.TextField(max_length=500,  blank=True, null=True)
    prise = models.DecimalField(
        max_digits=9, decimal_places=2, default=00.00, null=True, blank=True)
    img = models.ImageField(upload_to='static/images/',
                            default='static/images/placeholder/img.png')


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
