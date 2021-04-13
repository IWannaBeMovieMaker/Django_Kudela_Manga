from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


def attachment_path(instance, filename):
    return"film/"+ str(instance.manga.id) + "/attachments/"+ filename


class Type(models.Model):
    SHONEN = 'SHONEN'
    SHOJO = 'SHOJO'
    SEISEN = 'SEISEN'
    JOSEI = 'JOSEI'
    KODOMOMUKE = 'KODOMOMUKE'
    MANGAS_TYPES_CHOICES = (
        (SHONEN, 'Shonen'),
        (SHOJO, 'Shojo'),
        (SEISEN, 'Seinen'),
        (JOSEI, 'Josei'),
        (KODOMOMUKE, 'Kodomomuke'),
    )
    name = models.CharField(max_length=10, choices=MANGAS_TYPES_CHOICES, default=SHOJO, verbose_name="Type name")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Manga(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    author = models.CharField(max_length=100, verbose_name="Author")
    chapter = models.IntegerField(null=False, verbose_name="Chapter")
    plot = models.TextField(null=True, verbose_name="Plot")
    release_date = models.DateField(null=True,
                                    help_text="Please enter the release date of curent chapter",
                                    verbose_name="Release date")
    pages = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(400)],
                                help_text="Enter an integer representing number of pages", verbose_name="Pages")
    rating = models.FloatField(default=5, validators=[MinValueValidator(1), MaxValueValidator(10)], null=True,
                                help_text="Range 1-10 (10 is best, 1 is worst)", verbose_name="Rating")
    types = models.ManyToManyField(Type, help_text='Select a Type for this Manga')

    class Meta:
        ordering = ["-release_date", "title", "chapter"]

    def __str__(self):
        return f"{self.title}, {self.author}, {self.chapter},year: {str(self.release_date.year)}, rate: {str(self.rating)}"

    def get_absolute_url(self):
        return reverse('Manga-detail', args=[str(self.id)])


class Attachment(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    last_update = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to=attachment_path, null=True, verbose_name="File")

    TYPE_OF_ATTACHMENT = (
    ('Poster', 'Poster'),
    ('Opening', 'Opening'),
    ('text', 'Text'),
    ('video', 'Video'),
    ('other', 'Other'),
    ('Manga', 'Manga'),
    )

    type = models.CharField(max_length=7, choices=TYPE_OF_ATTACHMENT, default='Poster', help_text='Select allowed attachment type', verbose_name="Attachment type")

    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)


class Meta:
    ordering = ["-last_update", "type"]

    def __str__(self):
        return f"{self.title}, ({self.type})"