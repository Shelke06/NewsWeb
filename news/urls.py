from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sports/', views.sports, name='sports'),
    path('politics/', views.politics, name='politics'),
    path('entertainment/', views.entertainment, name='entertainment'),
    path('share-market/', views.share_market, name='share_market'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
]

