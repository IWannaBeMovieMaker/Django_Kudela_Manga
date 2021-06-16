from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mangas/', views.MangaListView.as_view(), name='mangas'),
    path('mangas/type/<str:type_name>/', views.MangaListView.as_view(), name='manga-type'),
    path('mangas/<int:pk>/', views.MangaDetailView.as_view(), name='manga-detail'),
    path('mangas/create/', views.MangaCreate.as_view(), name='manga-create'),
    path('mangas/<int:pk>/update/', views.MangaUpdate.as_view(), name='manga-update'),
    path('mangas/<int:pk>/delete/', views.MangaDelete.as_view(), name='manga-delete'),
    #path('mangas/<int:pk>/edit/', views.edit_manga, name='manga-edit'),
]
