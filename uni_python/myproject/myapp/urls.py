from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('info/', views.info, name='info'),
    path('attraction_list/', views.attraction_list, name='attraction_list'),
    path('add_attraction/', views.add_attraction, name='add_attraction'),
    path('edit_attraction/<int:pk>/', views.edit_attraction, name='edit_attraction'),
    path('delete_attraction/<int:pk>/', views.delete_attraction, name='delete_attraction'),
    path('category_list/', views.category_list, name='category_list'),
    path('add_category/', views.add_category, name='add_category'),
    path('edit_category/<int:pk>/', views.edit_category, name='edit_category'),
    path('delete_category/<int:pk>/', views.delete_category, name='delete_category'),
    path('event_list/', views.event_list, name='event_list'),
    path('add_event/', views.add_event, name='add_event'),
    path('edit_event/<int:pk>/', views.edit_event, name='edit_event'),
    path('delete_event/<int:pk>/', views.delete_event, name='delete_event'),
]