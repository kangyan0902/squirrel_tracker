from django.urls import path

from . import views

apps_name = 'sightings'
urlpatterns = [
    path('', views.list_of_squirrels, name='list_of_squirrels'),
    path('add/', views.add_squirrel, name = 'add'),
    path('stats/', views.stats, name='stats'),
    path('<str:squirrel_id>/', views.edit_squirrel, name='edit'),
    path('<str:pk>/delete/', views.delete_squirrel.as_view(), name='delete'),
]