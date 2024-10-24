from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('info/', views.info, name='info'),

    path('attractions/', views.attraction_list, name='attraction_list'),
    path('attractions/add/', views.add_attraction, name='add_attraction'),
    path('attractions/edit/<int:pk>/', views.edit_attraction, name='edit_attraction'),
    path('attractions/delete/<int:pk>/', views.delete_attraction, name='delete_attraction'),
    path('attractions/<int:pk>/', views.attraction_detail, name='attraction_detail'),

    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/edit/<int:pk>/', views.edit_category, name='edit_category'),
    path('categories/delete/<int:pk>/', views.delete_category, name='delete_category'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),

    path('events/', views.event_list, name='event_list'),
    path('events/add/', views.add_event, name='add_event'),
    path('events/edit/<int:pk>/', views.edit_event, name='edit_event'),
    path('events/delete/<int:pk>/', views.delete_event, name='delete_event'),
    path('events/<int:pk>/', views.event_detail, name='event_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)