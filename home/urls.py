from django.urls import path
from . import views  as local_views
from django.conf import settings
from django.conf.urls.static import static
from .views import get_name
from django.contrib.auth.views import LogoutView


urlpatterns = [	
	path('Login/', get_name.as_view(), name='login'),
	path('Logout/',LogoutView.as_view(next_page='index'), name='logout'),
	path('', local_views.home, name='index'),
	path('User-account/', local_views.profile),
	path('Carbon-footprint/', local_views.calculator),
	path('History-of-use/', local_views.historyofuse),
	path('Register/', local_views.register),

]