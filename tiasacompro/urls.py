from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500, handler403, handler400
#from appgrei.views import CustomPasswordChangeView

from django.shortcuts import redirect

# def login_redirect(request):
#     if request.user.is_authenticated:
#         return redirect('/simutu/')


urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    #path('simutu/', include('comproapp.urls')),
    # path(
    #     'password/change/',
    #     CustomPasswordChangeView.as_view(),
    #     name='password_change'
    # ),
    path('admin/', admin.site.urls),
    path('', include('comproapp.urls')),
]

handler404 = 'comproapp.views.handler404'
handler500 = 'comproapp.views.handler500'
handler403 = 'comproapp.views.handler403'
handler400 = 'comproapp.views.handler400'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)