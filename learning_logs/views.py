from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from learning_logs.models import Topic, Entry
from django.contrib.auth.decorators import login_required
from learning_logs.form import TopicForm, EntryForm
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')
@login_required
def topics(request):
    try:
        topics = Topic.objects.filter(owner = request.user).order_by('-date_added')
    except Topic.DoesNotExist:
        raise Http404
    context = {
        'topics':topics
    }
    return render(request, 'learning_logs/topics.html', context)
@login_required
def topic(request,topic_id):
    topic = get_object_or_404(Topic, pk = topic_id)
    if topic.owner != request.user:
            raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {
        'topic':topic,
        'entries':entries
    }
    return render(request, 'learning_logs/topic.html', context)
@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
       
    else:
        form = TopicForm(data = request.POST)
        if form.is_valid():
            #if topic.owner == request.user:
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)
@login_required
def new_entry(request,topic_id):
    topic = Topic.objects.get(pk= topic_id)
    if topic.owner != request.user:
            raise Http404
    if request.method != 'POST':
        form = EntryForm()
       
    else:
        form = EntryForm(data = request.POST)
        if form.is_valid():
                #if topic.owner == request.user:
                new_entry = form.save(commit=False)
                new_entry.topic = topic
                new_entry.save()
                return HttpResponseRedirect(reverse('learning_logs:topic', args = (topic.id,)))
    context = {'form':form,'topic':topic, }
    return render(request,'learning_logs/new_entry.html', context)

@login_required       
def edit_entry(request,entry_id):
    entry = Entry.objects.get(pk= entry_id)
    topic = entry.topic
    if topic.owner != request.user:
            raise Http404
    if request.method != 'POST':
        form = EntryForm(instance = entry)
       
        
    else:
        form = EntryForm(instance = entry,data = request.POST)
        if form.is_valid():
                #if topic.owner == request.user:
                new_entry = form.save(commit=False)
                new_entry.topic = topic
                new_entry.save()
                return HttpResponseRedirect(reverse('learning_logs:topic', args = (topic.id,)))
    context = {'form':form,'entry':entry, 'topic':topic}
    return render(request,'learning_logs/edit_entry.html', context)