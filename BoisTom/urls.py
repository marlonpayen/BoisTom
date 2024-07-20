"""
URL configuration for BoisTom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve 
from website import views
from django.conf.urls.static import static
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.conf import settings

def response_error_handler(request, exception=None):
    return HttpResponse("Error handler content", status=403)


def permission_denied_view(request):
    raise PermissionDenied

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('messagesent', views.send_message, name='form'),
    path("403/", permission_denied_view)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "website.views.my_custom_page_not_found_view"
handler500 = "website.views.my_custom_error_view"
handler403 = "website.views.my_custom_permission_denied_view"
handler400 = "website.views.my_custom_bad_request_view"
