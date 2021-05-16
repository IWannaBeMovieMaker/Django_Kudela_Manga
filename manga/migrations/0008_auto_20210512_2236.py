# Generated by Django 3.2 on 2021-05-12 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0007_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='manga/posters/%Y/%m/%d/', verbose_name='Poster'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='type',
            field=models.CharField(blank=True, choices=[('Opening', 'Opening'), ('text', 'Text'), ('video', 'Video'), ('other', 'Other'), ('Manga', 'Manga')], default='image', help_text='Select allowed attachment type', max_length=7, verbose_name='Attachment type'),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(max_length=10, verbose_name='Type name'),
        ),
    ]
