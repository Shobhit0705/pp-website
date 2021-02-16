from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homes'),
    path('home/', views.index, name='home'),
    path('examples/', views.example, name='examples'),
    path('my_project/', views.project, name='project'),
    path('citations/', views.citation, name='citations')

]