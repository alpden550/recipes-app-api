# Generated by Django 3.0.5 on 2020-04-24 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20200424_1411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='decription',
            new_name='description',
        ),
    ]
