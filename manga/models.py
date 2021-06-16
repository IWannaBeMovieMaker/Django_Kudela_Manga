from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.html import format_html


def attachment_path(instance, filename):
    return"manga/" + str(instance.manga.id) + "/attachments/" + filename


class Type(models.Model):
    name = models.CharField(max_length=10, null=False, verbose_name="Type name")

    class Meta:
        ordering = ["name"]
        verbose_name = "Type"
        verbose_name_plural = "Types"

    def __str__(self):
        return self.name

    def manga_count(self, obj):
        return obj.manga_set.count()


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
    poster = models.ImageField(upload_to='manga/posters/%Y/%m/%d/', blank=True, null=True, verbose_name="Poster")
    rating = models.FloatField(default=5, validators=[MinValueValidator(1), MaxValueValidator(10)], null=True,
                                help_text="Range 1-10 (10 is best, 1 is worst)", verbose_name="Rating")
    types = models.ManyToManyField(Type, help_text='Select a Type for this Manga')

    class Meta:
        ordering = ["-release_date", "title", "chapter"]

    def __str__(self):
        return f"{self.title}, {self.author}, {self.chapter},year: {str(self.release_date.year)}, rate: {str(self.rating)}"

    def get_absolute_url(self):
        return reverse('Manga-detail', args=[str(self.id)])

    def release_year(self):
        return self.release_date.year

    def rate_percent(self):
        return format_html("{} %", int(self.rate * 10))


class Attachment(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    last_update = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to=attachment_path, null=True, verbose_name="File")

    TYPE_OF_ATTACHMENT = (
    ('Opening', 'Opening'),
    ('text', 'Text'),
    ('video', 'Video'),
    ('other', 'Other'),
    ('Manga', 'Manga'),
    )

    type = models.CharField(max_length=7, choices=TYPE_OF_ATTACHMENT, blank=True, default='image', help_text='Select allowed attachment type', verbose_name="Attachment type")

    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)


class Meta:
    order_with_respect_to = 'manga'

    def __str__(self):
        return f"{self.title}, ({self.type})"
