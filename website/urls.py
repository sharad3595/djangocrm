from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path("", auth_views.LoginView.as_view(template_name = "user_login.html" ,redirect_authenticated_user=True),name="home"),
    #path('login/',views.login_user, name="login"),
    path('record/',views.record, name="record"),
    path('record/<int:pk>',views.single_record, name="single_record"),
    path('single_record_delete/<int:pk>',views.single_record_delete, name="single_record_delete"),
    path('add_record/',views.add_record, name="add_record"),
    path('update_record/<int:pk>',views.update_record, name="update_record"),
    path('logout/',views.logout_user, name="logout"),
    path('register/',views.sign_up_page, name="register"),
    path('dashboard/', views.dashboard, name="dashboard")
   
]
