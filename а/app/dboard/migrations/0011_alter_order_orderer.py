# Generated by Django 4.1.2 on 2022-10-21 05:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dboard', '0010_order_orderer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
