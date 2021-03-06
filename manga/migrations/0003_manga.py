# Generated by Django 3.2 on 2021-04-13 18:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0002_rename_types_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('author', models.CharField(max_length=100, verbose_name='Author')),
                ('chapter', models.IntegerField(blank=True, verbose_name='Chapter')),
                ('plot', models.TextField(blank=True, null=True, verbose_name='Plot')),
                ('release_date', models.DateField(blank=True, help_text='Please enter the release date of curent chapter', null=True, verbose_name='Release date')),
                ('pages', models.IntegerField(blank=True, help_text='Enter an integer representing number of pages', null=True, verbose_name='Pages')),
                ('rating', models.FloatField(default=50, help_text='Range 1-10 (10 is best, 1 is worst)', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Rating')),
                ('types', models.ManyToManyField(help_text='Select a Type for this Manga', to='manga.Type')),
            ],
            options={
                'ordering': ['-release_date', 'title', 'chapter'],
            },
        ),
    ]
