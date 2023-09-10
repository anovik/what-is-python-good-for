from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('chapters/', views.chapters, name='chapters'),       
    path('chapters/chapter/<int:id>', views.chapter, name='chapter'),
]