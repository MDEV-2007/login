
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import frontpage,signup,accounts

from django.contrib.auth import views

urlpatterns = [
    path('',frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(),name='logout'),
     path('login/', views.LoginView.as_view(template_name='core/login.html'),name='login'),
    path('admin/', admin.site.urls),
    path('accounts/',  accounts, name='accounts')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
