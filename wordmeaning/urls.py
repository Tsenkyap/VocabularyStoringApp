from django.urls import path
from . import views

app_name = 'wordmeaning'

urlpatterns = [
		path('', views.main , name='main'),
		path('entries/', views.entries , name='entries'),
		path('entries/<int:pk>/update/', views.update_entries , name='update_entries'),
		path('entries/<int:pk>/delete/', views.delete_entries , name='delete_entries'),
	]