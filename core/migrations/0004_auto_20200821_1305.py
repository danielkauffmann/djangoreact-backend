# Generated by Django 3.1 on 2020-08-21 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_item_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
