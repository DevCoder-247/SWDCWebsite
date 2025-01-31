from django.contrib import admin
from django.urls import path, include, re_path
from . import views
import authentication.views_authentication as views_a
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('receivedata', views.receivedata),
    path('', views_a.LoginView, name='login'),
    path('FAQs', views.FAQsView, name='faqs'),
    path('home', views.homeView, name='home'),
    path('user-manual', views.showLinksView, name='user-manual'),
    path('admin/', admin.site.urls),
    path('action/', include('action.urls')),
    path('a/', include('authentication.urls')),
    path('v/', include('Volunteer.urls')),
    path('c/', include('Coordinator.urls')),
    path('s/', include('Secretary.urls')),
    re_path(r'^500/$', views.custom_500_error_view, name='custom_500_error'),
]
handler404 = 'SWDCWebsite.views.custom_404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()