from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('article/', include('article.urls', namespace='article')),
    path('account/', include('account.urls', namespace='account')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # just and just in developing mode not at all in production mode

