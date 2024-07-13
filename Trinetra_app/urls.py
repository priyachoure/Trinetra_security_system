from django.urls import path
from . import views

urlpatterns = [
    # path('', views.Base, name='base'),
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('services/', views.service, name='services'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('career/', views.career, name='career'),
    path('career_form/', views.Career_form, name='career_form'),
    # path('about', views.About, name='about'),


    # our solutions link--------

    path('access_control/', views.Enterprise_acess_control_systems, name='access_control'),
    path('video_servillance/', views.Enterprise_video_servillance, name='video_servillance'),
    path('fire_alaram_detection/', views.Enterprise_fire_alaram_detection, name='fire_alaram_detection'),
    path('Data_center/', views.Enterprise_Data_center_solution, name='Data_center'),
    path('integrated_security/', views.integrated_security, name='integrated_security'),
    path('visitor_management/', views.visitor_management_systems, name='visitor_management'),
    path('barier_based/', views.Barier_basedd_solution, name='barier_based'),
    path('touchless_access/', views.touchless_access, name='touchless_access'),
    path('Web_development/', views.Enterprise_Web_development, name='Web_development'),
    path('digital_marketing/', views.Enterprise_digital_marketing, name='digital_marketing'),
    path('web_designing/', views.Enterprise_web_designing, name='web_designing'),
    path('App_development/', views.Enterprise_App_development, name='App_development'),






]
