from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Type, Manga, Attachment


class MangaModelForm(ModelForm):
    def clean_runtime(self):
        data = self.cleaned_data['pages']
        if data <= 0:
            raise ValidationError('Invalid number of pages')
        return data

    def clean_rate(self):
        data = self.cleaned_data['rating']
        if data < 1 or data > 10:
            raise ValidationError('Invalid rating: must be in the range 1-10')
        return data

    class Meta:
        model = Manga
        fields = ['title', 'plot', 'chapter', 'plot', 'release_date', 'pages', 'poster', 'rating', 'types']
        labels = {'title': 'Manga name', 'Author': 'Plot'}


"""
class FilmForm(forms.Form):
    title = forms.CharField(label='Název filmu', help_text='Zadejte název filmu', required=True)
    plot = forms.CharField(label='Stručný děj', required=False)
    release_date = forms.DateField(label='Datum uvedení', required=True)
    runtime = forms.IntegerField(label='Délka filmu', required=False, help_text='Uveďte počet minut')
    poster = forms.ImageField(label='Plakát', required=False, help_text='Vkládejte grafické formáty')
    FILM_RATE = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    rate = forms.ChoiceField(choices=FILM_RATE, label='Hodnocení')
    genres = forms.ModelMultipleChoiceField(queryset = Genre.objects.all())
"""
