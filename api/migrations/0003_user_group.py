# Generated by Django 3.0.5 on 2020-04-21 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('api', '0002_auto_20200421_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='auth.Group', verbose_name='Group'),
        ),
    ]
