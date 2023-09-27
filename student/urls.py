from .import views
from django.urls import path, include

urlpatterns = [
    path('home/', views.student_home_data, name='home'),
    path('showdata/', views.student_show_data, name='showdata'),
    path('createdata/', views.student_create_data, name='createdata'),
    path('editdata/<int:id>/', views.student_edit_data, name='editdata'),
    path('deldata/<int:id>/', views.student_del_data, name='deldata'),
    path('signup/', views.signupModal, name='signup'),
    path('login/', views.loginModal, name='login'),
    path('logout/', views.logoutModal, name='logout'),
    path('', views.student_login_logout_data, name='loginsignup'),
]