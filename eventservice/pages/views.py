from django.shortcuts import render, get_object_or_404, redirect
from .forms import EventForm, CommentForm
from django.views.generic import (ListView, DetailView, DeleteView, CreateView, UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework import viewsets
from .models import Events




class EventListView(ListView):
    model = Events
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    ordering = ['-published_date']



class EventDetailView(DetailView):
    model = Events
    context_object_name = 'events'
    template_name = 'events/event_detail.html'


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Events
    fields = ['public', 'title','start_date', 'end_date', 'location', 'text']
    template_name = 'events/event_edit.html'
    login_url = '/login'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Events
    fields = ['title', 'start_date', 'end_date', 'text', 'location']
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
        events = self.get_object()
        if self.request.user == events.author:
            return True
        return False


def add_comment_to_event(request, pk):
    event = get_object_or_404(Events, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.event = event
            comment.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = CommentForm()
    return render(request, 'events/add_comment_to_event.html', {'form': form, 'event': event})


def about(request):
    return render(request, 'events/about.html', {'title': 'About'})


# Create your views here.
