from django.contrib import admin

from django.db.models import Count
from django.utils.html import format_html

from .models import *


@admin.register(Type)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "manga_count")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _manga_count=Count("manga", distinct=True),
        )
        return queryset

    def manga_count(self, obj):
        return obj._manga_count

    manga_count.admin_order_field = "_manga_count"
    manga_count.short_description = "Manga count"


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ("title", "release_year", "rate_percent")

    def release_year(self, obj):
        return obj.release_date.year

    def rate_percent(self, obj):
        return format_html("<b>{} %</b>", int(obj.rating * 10))

    rate_percent.short_description = "Manga rating"
    release_year.short_description = "release year"


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "manga_title")

    def manga_title(self, obj):
        return obj.manga.title

        @admin.register(Review)
        class ReviewAdmin(admin.ModelAdmin):
            list_display = ("author", "manga", "rate", "edit_date")