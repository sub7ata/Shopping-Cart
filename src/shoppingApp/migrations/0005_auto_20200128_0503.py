# Generated by Django 3.0.2 on 2020-01-28 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingApp', '0004_auto_20200128_0423'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['-id']},
        ),
        migrations.RemoveField(
            model_name='cart',
            name='date_ordered',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='is_ordered',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='ref_code',
        ),
    ]
