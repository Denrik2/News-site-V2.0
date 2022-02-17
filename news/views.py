from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Articles.objects.all()
    return render(request, 'news/news_home.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'НЕВЕРНО ВЫПОЛНЕНА ФОРМА'
    form = ArticlesForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)


class NewsDetail(DetailView):
    model = Articles
    template_name = 'news/NewsDetail.html'
    context_object_name = 'articles'


class NewsUpdate(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm


class NewsDelete(DeleteView):
    model = Articles
    template_name = 'news/delete.html'
    success_url = '/news'
