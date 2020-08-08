from django.shortcuts import render
from .forms import EventForm, CommentForm
from .models import Events
from django.views.generic import (ListView, DetailView, DeleteView, CreateView, UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import Events
from django.shortcuts import render, get_object_or_404, redirect


class EventListView(ListView):
    model = Events
    template_name = 'events/base.html'
    context_object_name = 'events'


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Events
    fields = ['public', 'title', 'text']
    template_name = 'events/event_edit.html'
    login_url = '/login'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EventDetailView(DetailView):
    model = Events
    template_name = 'events/events_detail.html'

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Events
    fields = ['title', 'text']
    template_name = 'events/event_edit.html'
    login_url = '/login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Events
    success_url = '/'

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False


def add_comment_to_event(request, pk):
    event = get_object_or_404(Events, pk=pk)
    if request.method == "EVENT":
        form = CommentForm(request.EVENTS)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.event = event
            comment.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = CommentForm()
    return render(request, 'events/add_comment_to_event.html', {'form': form})

# Create your views here.
