from django.urls import path
from . import views


app_name = 'web'

urlpatterns = [
    path('', views.index,name="index"),
    path('about/', views.about,name="about"),
    path('services/', views.services,name="services"),
    path('portfolio/', views.portfolio,name="portfolio"),
    path('blog/', views.blog,name="blog"),
    path('blog-details/<str:slug>/', views.blog_details,name="blog_details"),
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
    path('residential-cleaning/', views.residential_cleaning,name="residential_cleaning"),
    path('sofa-cleaning/', views.sofa_cleaning,name="sofa_cleaning"),
    path('construction-cleaning/', views.construction_cleaning,name="construction_cleaning"),
    path('carpet-cleaning/', views.carpet_cleaning,name="carpet_cleaning"),
    path('mattress-cleaning/', views.mattress_cleaning,name="mattress_cleaning"),
    path('office-cleaning/', views.office_cleaning,name="office_cleaning"),

]

    