from django.urls import path
from . import views

app_name = 'tools'

urlpatterns = [
    # Function Based Views
    path('', views.tool_list, name='tool_list_fbv'),
    path('<int:tool_id>/', views.tool_detail, name='tool_detail_fbv'),
    
    # Class Based Views
    path('cbv/', views.ToolListView.as_view(), name='tool_list_cbv'),
    path('cbv/<int:pk>/', views.ToolDetailView.as_view(), name='tool_detail_cbv'),
]