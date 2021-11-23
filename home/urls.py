from django.urls import path
from . import views  as local_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', local_views.home),
	path('User-account/', local_views.profile),
	path('Carbon-footprint/', local_views.calculator),
	path('History-of-use/', local_views.historyofuse),
	path('Register/', local_views.register),
]