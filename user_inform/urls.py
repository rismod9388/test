from django.urls import path
from . import views

app_name = 'user_inform'

urlpatterns = [
   #path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('',views.information,name='information') ,
    path('modifyinform/',views.profile_update_view, name='profile_update') ,
    path('modifypw/',views.password_edit_view, name='password_edit') ,
]