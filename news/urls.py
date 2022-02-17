from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetail.as_view(), name='NewsDetail'),
    path('<int:pk>/update', views.NewsUpdate.as_view(), name='NewsUpdate'),
    path('<int:pk>/delete', views.NewsDelete.as_view(), name='Newsdelete'),

]
