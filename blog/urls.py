from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.article_detail, name='article_detail'),
    path('blog/<int:pk>/modifier/', views.article_modifier, name='article_modifier'),
    path('blog/<int:pk>/supprimer/', views.article_supprimer, name='article_supprimer'),
]