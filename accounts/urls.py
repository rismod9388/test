from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
   #path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
   path('login/', views.LoginView.as_view(), name='login'),
   path('logout/',views.logout_view,name='logout') ,
   path('signup/', views.CsRegisterView.as_view(), name='signup'),
]
