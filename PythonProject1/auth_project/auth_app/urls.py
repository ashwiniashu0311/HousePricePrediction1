from django.urls import path
from . import views
urlpatterns = [

    path('',views.home),
    path('register/',views.register_view,name='register'),
    path('login/', views.login_view, name='login'),
    path('admin_login/', views.admin_login_view, name='admin_login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('predict/',views.predict, name='predict'),
    path('predict/result/', views.result),
    path('about/',views.about),
    path('contact/', views.contact),
    path('admin/users',views.redirect_to_users),

]
