from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('postings.urls')),
    path('games/', include('games.urls')),
    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG == False:
    urlpatterns += re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),