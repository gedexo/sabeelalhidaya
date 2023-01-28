from django.urls import path
from . import views


app_name = 'web'

urlpatterns = [
    path('', views.index,name="index"),
    path('about/', views.about,name="about"),
    path('services/', views.services,name="services"),
    path('gallery/', views.gallery,name="gallery"),
    path('contact/', views.contact,name="contact"),

    path('ac-service/', views.ac_service,name="ac_service"),
    path('electrical-service/', views.electrical_service,name="electrical_service"),
    path('plumber-service/', views.plumbing_service,name="plumbing_service"),

    path('tiling-service/', views.tiling_service,name="tiling_service"),
    path('carpentry-service/', views.carpentry_service,name="carpentry_service"),
    path('general-maintanace/', views.general_maintanance,name="general_maintanance"),
    path('building-cleaning/', views.building_cleaning_service,name="building_cleaning_service"),
    path('painting-service/', views.painting_service,name="painting_service"),

    path('wallpaper-fixing/', views.wallpaper_fixing,name="wallpaper_fixing"),
    path('masonry/', views.masonry_service,name="masonry_service"),

]

    