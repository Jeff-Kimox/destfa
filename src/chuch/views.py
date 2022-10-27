from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from .models import Sermon, Event, User
from .forms import CustomUserCreationForm

# Create your views here.

def register_page(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("form is valid")
            

    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def login_page(request):
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('index')


def index(request):
    queryset = Sermon.objects.filter(featured=True)
    events = Event.objects.filter(featured=True)
    context = {
        'object_list': queryset,
        'events': events,
    }
    return render(request, 'index.html', context)

def events(request):
    events = Event.objects.filter(featured=True)
    event_list = Event.objects.all()
    paginator = Paginator(event_list, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'events': events,
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'events.html', context)


def sermons(request):
    sermons = Sermon.objects.all()
    paginator = Paginator(sermons, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermons.html', context)


def sermon_detail(request, id):
    sermon = Sermon.objects.get(pk=id)
    latest = Sermon.objects.order_by('-timestamp')[:3]
    queryset = Sermon.objects.all()
    context = {
        "sermon": sermon,
        "latest": latest,
        "queryset": queryset
    }
    return render(request, "sermon_detail.html", context)


def event_detail(request, id):
    event = Event.objects.get(pk=id)
    context = {
        "event": event,
    }
    return render(request, "event_detail.html", context)




# def events(request):
#     events = Event.objects.filter(featured=True)
#     context = {
#         'object_list': events
#     }
#     return render(request, 'evtd.html', context)
