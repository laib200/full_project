# Generated by Django 4.2.2 on 2023-06-25 16:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_products_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='id',
            field=models.UUIDField(default=uuid.UUID('910b0382-06bf-4e31-abd6-f9c15d896589'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]