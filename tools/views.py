from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Tool

# Function Based Views
def tool_list(request):
    """FBV - Display all tools"""
    tools = Tool.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        tools = tools.filter(name__icontains=search_query)
    
    # Filter by category
    category = request.GET.get('category', '')
    if category:
        tools = tools.filter(category__icontains=category)
    
    # Filter trending
    if request.GET.get('trending'):
        tools = tools.filter(is_trending=True)
    
    context = {
        'tools': tools,
        'search_query': search_query,
        'category': category,
    }
    return render(request, 'tools/tool_list.html', context)

def tool_detail(request, tool_id):
    """FBV - Display single tool"""
    tool = get_object_or_404(Tool, id=tool_id)
    return render(request, 'tools/tool_detail.html', {'tool': tool})

# Class Based Views
class ToolListView(ListView):
    """CBV - List all tools"""
    model = Tool
    template_name = 'tools/tool_list.html'
    context_object_name = 'tools'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset

class ToolDetailView(DetailView):
    """CBV - Display single tool"""
    model = Tool
    template_name = 'tools/tool_detail.html'
    context_object_name = 'tool'
    pk_url_kwarg = 'pk'