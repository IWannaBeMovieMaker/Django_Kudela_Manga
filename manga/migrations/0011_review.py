# Generated by Django 3.1.7 on 2021-06-21 20:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0010_auto_20210616_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
                ('edit_date', models.DateTimeField(auto_now=True)),
                ('rate', models.IntegerField(default=5, help_text='Please enter an integer value (range 1 - 10)', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Rate')),
                ('manga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manga.manga')),
            ],
            options={
                'order_with_respect_to': 'manga',
            },
        ),
    ]
