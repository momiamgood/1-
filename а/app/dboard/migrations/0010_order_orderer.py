# Generated by Django 4.1.2 on 2022-10-21 05:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dboard', '0009_alter_order_order_img_additionalimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
