from . import views
from django.urls import path


urlpatterns = [
    path('', views.about_views, name='about'),
]