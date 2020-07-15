from django.conf.global_settings import STATIC_ROOT
from django.conf.urls import url
from django.urls import path

from Experiment2 import settings
from . import views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-book'),
    path('updates/<int:book_id>', views.update_book),
    path('deletes/<int:book_id>', views.delete_book),
    url(r'^login/$', auth_views.LoginView.as_view(template_name= 'crudApp2/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page= '/login'), name='logout'),
    path('signup/', views.signup_view, name="signup"),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]

if settings.DEBUG:
       urlpatterns += static(settings.MEDIA_URL,
                             document_root=settings.MEDIA_ROOT)
