from django.urls import path
from .views import ArticleView, ArticleDetailView
urlpatterns = [
    path('', ArticleView.as_view(), name='articles'),
    path('<str:slug>', ArticleView.as_view(), name='articles'),
    path('detail/<str:slug>', ArticleDetailView.as_view(), name='detail'),
]