"""mangacomics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import django
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
import manga

urlpatterns = [
path('admin/', admin.site.urls),
path('manga/', include('manga.urls')),
path('', RedirectView.as_view(url='manga/')),
path('accounts/', include('accounts.urls')),
path('accounts/', include('django.contrib.auth.urls')),
                ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'manga.views.error_404'
handler500 = 'manga.views.error_500'
handler403 = 'manga.views.error_403'
handler400 = 'manga.views.error_400'

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
    urlpatterns += [re_path(r'^500/$', manga.views.error_500)]
    urlpatterns += [re_path(r'^400/$', manga.views.error_400)]
    urlpatterns += [re_path(r'^404/$', manga.views.error_404)]
    urlpatterns += [re_path(r'^403/$', manga.views.error_403)]

admin.site.site_header = "MD Administration"
admin.site.site_title = "Manga database"
admin.site.index_title = "Welcome to administration part of MD"
