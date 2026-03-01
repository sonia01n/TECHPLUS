from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    # Function Based Views
    path('', views.news_list, name='news_list_fbv'),
    path('<int:news_id>/', views.news_detail, name='news_detail_fbv'),
    
    # Class Based Views
    path('cbv/', views.NewsListView.as_view(), name='news_list_cbv'),
    path('cbv/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail_cbv'),
]