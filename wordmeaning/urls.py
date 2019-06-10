from django.urls import path
from . import views

app_name = 'wordmeaning'

urlpatterns = [
		path('', views.main , name='main'),
		path('entries', views.entries , name='entries'),
	]