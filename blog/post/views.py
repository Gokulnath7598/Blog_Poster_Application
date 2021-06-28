from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Entry

# Create your views here.
class HomeView(LoginRequiredMixin,ListView):
    model = Entry
    template_name = 'post/index.html'
    context_object_name = "blog_entries"
    ordering = ['-date']
    paginate_by = 3

class EntryView(LoginRequiredMixin,DetailView):
    model = Entry
    template_name = 'post/entry_detail.html'
    

class CreateEntryView(LoginRequiredMixin,CreateView):
    model = Entry
    template_name = 'post/create.html'
    fields = ['title','text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
