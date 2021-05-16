from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mangas/', views.MangaListView.as_view(), name='mangas'),
    path('mangas/types/<str:type_name>/', views.MangaListView.as_view(), name='manga_type'),
    path('mangas/<int:pk>/', views.MangaDetailView.as_view(), name='manga_detail'),
]
