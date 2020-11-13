from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('create/', views.article_create, name='create'),
    path('<int:id>/', views.article_detail, name='detail'),
    path('<int:id>/edit/', views.article_edit, name='edit'),
    path('<int:id>/delete/', views.article_delete, name='delete'),
]
