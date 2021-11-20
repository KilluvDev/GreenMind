from django.urls import path
from . import views  as local_views

urlpatterns = [
	path('', local_views.home, name='home'),
	path('User-account/', local_views.historyofuse),
	path('Carbon-footprint/', local_views.home),
	path('History-of-use/', local_views.home)
]