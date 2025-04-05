import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from news.forms import LogMessageForm
from news.models import LogMessage
from django.views.generic import ListView
from .models import News
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.paginator import Paginator


class HomeListView(ListView):
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "news/log_message.html", {"form": form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') 
    else:
        form = AuthenticationForm()
    return render(request, 'news/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'news/signup.html', {'form': form})

def home(request):
    news_list = News.objects.all().order_by('-created_at')
    return render(request, 'news/home.html', {'news_list': news_list})

def sports(request):
    sports_news_list = News.objects.filter(category='sports').order_by('-created_at')
    return render(request, 'news/sports.html', {'sports_news_list': sports_news_list})

def politics(request):
    politics_news_list = News.objects.filter(category='politics').order_by('-created_at')
    return render(request, 'news/politics.html', {'politics_news_list': politics_news_list})

def entertainment(request):
    entertainment_news_list = News.objects.filter(category='entertainment').order_by('-created_at')
    return render(request, 'news/entertainment.html', {'entertainment_news_list': entertainment_news_list})

def share_market(request):
    share_market_news_list = News.objects.filter(category='share_market').order_by('-created_at')
    return render(request, 'news/share_market.html', {'share_market_news_list': share_market_news_list})

def news_detail(request, pk):
    news = News.objects.get(pk=pk)
    return render(request, 'news/news_detail.html', {'news': news})
