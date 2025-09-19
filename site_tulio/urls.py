from site_tulio import views
from django.urls import path


urlpatterns = [
    path('', views.listaPost.as_view(), name = 'inicio'),
    path('postar/', views.novoPost.as_view(), name = 'postar'),
]