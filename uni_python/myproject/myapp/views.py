from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
import requests
from datetime import datetime
from .github_api import get_github_data
from .forms import AttractionForm, CategoryForm, EventForm
from .models import Attraction, Category, Event


def index(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

def info(request):
    username = 'Sb1414'
    github_data = get_github_data(username)
    return render(request, 'myapp/info.html', {'github_data': github_data})

def attraction_list(request):
    sort_by = request.GET.get('sort_by', 'name')
    if sort_by not in ['name', 'description', 'price', 'category']:
        sort_by = 'name'

    attractions = Attraction.objects.all().order_by(sort_by)
    form = AttractionForm()
    return render(request, 'myapp/attraction_list.html', {'attractions': attractions, 'form': form, 'sort_by': sort_by})

def add_attraction(request):
    if request.method == 'POST':
        form = AttractionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('attraction_list')
    else:
        form = AttractionForm()
    return render(request, 'myapp/add_attraction.html', {'form': form})

def edit_attraction(request, pk):
    attraction = get_object_or_404(Attraction, pk=pk)
    if request.method == 'POST':
        form = AttractionForm(request.POST, request.FILES, instance=attraction)
        if form.is_valid():
            form.save()
            return redirect('attraction_list')
    else:
        form = AttractionForm(instance=attraction)
    return render(request, 'myapp/edit_attraction.html', {'form': form})

def delete_attraction(request, pk):
    attraction = get_object_or_404(Attraction, pk=pk)
    if request.method == 'POST':
        attraction.delete()
        return redirect('attraction_list')
    return render(request, 'myapp/delete_attraction.html', {'attraction': attraction})

def category_list(request):
    sort_by = request.GET.get('sort_by', 'name')
    if sort_by not in ['name', 'description']:
        sort_by = 'name'

    categories = Category.objects.all().order_by(sort_by)
    form = CategoryForm()
    return render(request, 'myapp/category_list.html', {'categories': categories, 'form': form, 'sort_by': sort_by})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'myapp/add_category.html', {'form': form})

def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'myapp/edit_category.html', {'form': form})

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'myapp/delete_category.html', {'category': category})

def event_list(request):
    sort_by = request.GET.get('sort_by', 'name')
    if sort_by not in ['name', 'description', 'date', 'time', 'attraction']:
        sort_by = 'name'

    events = Event.objects.filter(is_active=True).order_by(sort_by)
    form = EventForm()
    return render(request, 'myapp/event_list.html', {'events': events, 'form': form, 'sort_by': sort_by})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'myapp/add_event.html', {'form': form})

def edit_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'myapp/edit_event.html', {'form': form})

def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'myapp/delete_event.html', {'event': event})

def attraction_detail(request, pk):
    attraction = get_object_or_404(Attraction, pk=pk)
    return render(request, 'myapp/attraction_detail.html', {'attraction': attraction})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'myapp/category_detail.html', {'category': category})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'myapp/event_detail.html', {'event': event})
