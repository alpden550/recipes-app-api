# Generated by Django 3.0.5 on 2020-04-23 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_ingredient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('time_minutes', models.PositiveIntegerField(verbose_name='Minutes')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price')),
                ('link', models.URLField(blank=True, max_length=255, verbose_name='Link')),
                ('ingredients', models.ManyToManyField(related_name='recipes', to='api.Ingredient', verbose_name='Ingredients')),
                ('tags', models.ManyToManyField(related_name='recipes', to='api.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Recipe',
                'verbose_name_plural': 'Recipes',
            },
        ),
    ]
