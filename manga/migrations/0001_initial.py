# Generated by Django 3.2 on 2021-04-13 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('SHON', 'Shonen'), ('SHOJ', 'Shojo'), ('SEIS', 'Seinen'), ('JOSE', 'Josei'), ('KODO', 'Kodomomuke')], default='SHOJ', max_length=4, verbose_name='Type name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
