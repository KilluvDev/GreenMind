from django.urls import path

from GreenMind import views as local_views

# path('Green-mind/',local_views.),

urlpatterns = [
    path('Green-mind/', local_views.home),
    path('Green-mind/Calcula-tu-huella/',local_views.form),
    path('Green-mind/User-account/',local_views.useracc),
    path('Green-mind/History-of-use/',local_views.history),
]
