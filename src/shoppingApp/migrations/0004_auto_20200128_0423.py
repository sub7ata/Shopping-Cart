# Generated by Django 3.0.2 on 2020-01-28 04:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shoppingApp', '0003_order'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Cart',
        ),
    ]
