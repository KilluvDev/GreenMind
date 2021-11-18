from django.urls import path

from GreenMind import views as local_views

urlpatterns = [
    path('GreenMind/', local_views.home),
]
