from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.cache import never_cache
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator

from manga.forms import MangaModelForm
from manga.models import Manga, Type, Attachment


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_mangas = Manga.objects.all().count()
    mangas = Manga.objects.order_by('-rating')[:10]

    context = {
        'num_mangas': num_mangas,
        'mangas': mangas
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class MangaListView(ListView):
    model = Manga

    context_object_name = 'mangas_list'
    template_name = 'manga/list.html'
    paginate_by = 6

    def get_queryset(self):
        if 'type_name' in self.kwargs:
            return Manga.objects.filter(types__name=self.kwargs['type_name']).all()
        else:
            return Manga.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_mangas'] = len(self.get_queryset())
        if 'type_name' in self.kwargs:
            context['view_title'] = f"Type: {self.kwargs['type_name']}"
            context['view_head'] = f"Manga Type: {self.kwargs['type_name']}"
        else:
            context['view_title'] = 'Mangas'
            context['view_head'] = 'Manga overview'
        return context


class MangaDetailView(DetailView):
    model = Manga
    context_object_name = 'manga_detail'
    template_name = 'manga/detail.html'


class TypeListView(ListView):
    model = Type
    template_name = 'blocks/type_list.html'
    context_object_name = 'types'
    queryset = Type.objects.order_by('name').all()


class TopTenListView(ListView):
    model = Manga
    template_name = 'blocks/top_ten.html'
    context_object_name = 'mangas'
    queryset = Manga.objects.order_by('-rating').all()[:10]


class NewMangaListView(ListView):
    model = Manga
    template_name = 'blocks/new_mangas.html'
    context_object_name = 'mangas'
    queryset = Manga.objects.order_by('release_date').all()
    paginate_by = 2


class MangaCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Manga
    template_name = 'manga/manga_bootstrap_form.html'
    fields = ['title', 'author', 'plot', 'chapter', 'plot', 'release_date', 'pages', 'poster', 'rating', 'types']
    initial = {'rating': '5'}
    success_url = reverse_lazy('mangas')
    login_url = '/accounts/login/'
    permission_required = 'manga.add_manga'


class MangaUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Manga
    template_name = 'manga/manga_bootstrap_form.html'
    form_class = MangaModelForm
    success_url = reverse_lazy('mangas')
    login_url = '/accounts/login/'
    permission_required = 'manga.change_manga'


class MangaDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Manga
    success_url = reverse_lazy('mangas')
    login_url = '/accounts/login/'
    permission_required = 'manga.delete_manga'


def error_404(request, exception=None):
    return render(request, 'errors/404.html')


def error_500(request):
    return render(request, 'errors/500.html')


def error_403(request, exception=None):
    return render(request, 'errors/403.html')


def error_400(request, exception=None):
    return render(request, 'errors/400.html')


@never_cache
def clear_cache(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    cache.clear()
    return HttpResponse('Cache has been cleared')
