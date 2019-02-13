from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='parkings'),
    path('<int:parking_id>', views.parking, name='parking'),
    path('search', views.search, name='search'),

]