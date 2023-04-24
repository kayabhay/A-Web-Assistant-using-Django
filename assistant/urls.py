from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('error-handler/',views.error_handler, name='error_handler')
]