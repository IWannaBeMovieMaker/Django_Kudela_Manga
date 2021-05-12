from django.shortcuts import render
from manga.models import Manga, Attachment


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_mangas = Manga.objects.all().count()
    mangas = Manga.objects.order_by('-rating')[:4]

    context = {
        'num_mangas': num_mangas,
        'mangas': mangas
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def topten(request):
    """
    View function for home page of site.
    """
    # Render the HTML template index.html
    return render(
        request,
        'topten.html',
    )