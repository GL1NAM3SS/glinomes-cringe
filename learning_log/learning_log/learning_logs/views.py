from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Topic
from .forms import TopicForm
from django.views.generic import DetailView, UpdateView


def index(request):
    """homepage"""
    return render(request, 'learning_logs/index.html')


def hui(request):
    """hui"""
    return HttpResponse("HUI")


def new_topic(request):
    """new topic"""
    if request.method != 'POST':
        # Data has not send; create empty form
        form = TopicForm()
    else:
        # POST data sended; Data working
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('topics')

    content = {'form': form}
    return render(request, 'learning_logs/new_topic.html', content)


def topics(request):
    """topics"""
    title = 'topics homepage'
    topics = Topic.objects.all()
    ctx = {'topics': topics, 'title': title}
    return render(request, 'learning_logs/topics.html', ctx)


class TopicsDetailView(DetailView):
    model = Topic
    template_name = 'learning_logs/topic_detail_view.html'
    context_object_name = 'topic_detail_view'


class TopicsUpdateView(UpdateView):
    model = Topic
    template_name = 'learning_logs/new_topic.html'
    fields = ['text']

