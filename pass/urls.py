from django.urls import path
from . import views



urlpatterns=[
    path("",views.home,name='home'),
    path("student",views.student,name='student'),
    path("incharge",views.incharge,name='incharge'),
    path("Hod",views.hod,name='hod'),
    path("warden",views.warden,name='warden'),
    path("security",views.security,name='security'),
    path('update_status', views.update_status, name='update_status'),
    path('success', views.success, name='success_url'),
    path('update_statuss', views.update_hod_status, name='update_hod_status'),
    path('qr', views.generate_qr_code, name='qr'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout, name='logout'),
    path('scan/', views.scan_qr_code, name='scan_qr_code'),
    

]