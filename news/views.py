from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import NewsArticle
from tools.models import Tool

# Function Based Views
def news_list(request):
    """FBV - Display all news"""
    news = NewsArticle.objects.all()
    
    # Filter by related tool
    tool_id = request.GET.get('tool')
    if tool_id:
        news = news.filter(related_tool_id=tool_id)
    
    # Filter by source
    source = request.GET.get('source')
    if source:
        news = news.filter(source__icontains=source)
    
    context = {
        'news': news,
        'tools': Tool.objects.all(),
    }
    return render(request, 'news/news_list.html', context)

def news_detail(request, news_id):
    """FBV - Display single news"""
    article = get_object_or_404(NewsArticle, id=news_id)
    return render(request, 'news/news_detail.html', {'article': article})

# Class Based Views
class NewsListView(ListView):
    """CBV - List all news"""
    model = NewsArticle
    template_name = 'news/news_list.html'
    context_object_name = 'news'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.all()
        return context

class NewsDetailView(DetailView):
    """CBV - Display single news"""
    model = NewsArticle
    template_name = 'news/news_detail.html'
    context_object_name = 'article'
    pk_url_kwarg = 'pk'