from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Sermon, Event, User, Message
from .forms import CustomUserCreationForm, SermonForm, EventForm

# Create your views here.


class RegisterView(generic.CreateView):
    template_name = "register.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


def register_page(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("login")
        else:
            messages.error(request, 'An error occurred during registartion')
            

    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'The User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username or password does not exist')

    context = {
        'page': page
    }
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

def youth_page(request):
    events = Event.objects.filter(categories='YOUTH')
    paginator = Paginator(events, 4)
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
    return render(request, 'youth.html', context)


def men_page(request):
    events = Event.objects.filter(categories='MEN')
    paginator = Paginator(events, 4)
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
    return render(request, 'men_page.html', context)

def women_page(request):
    events = Event.objects.filter(categories='WOMEN')
    paginator = Paginator(events, 4)
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
    return render(request, 'women_page.html', context)


def children_page(request):
    events = Event.objects.filter(categories='CHILDREN')
    paginator = Paginator(events, 4)
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
    return render(request, 'children_page.html', context)


def events(request):
    event_list = Event.objects.filter(categories='CHURCH')
    paginator = Paginator(event_list, 4)
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
    sermons = Sermon.objects.filter(categories='SERMON')
    paginator = Paginator(sermons, 4)
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


def bible_study(request):
    sermons = Sermon.objects.filter(categories='BIBLESTUDY')
    paginator = Paginator(sermons, 4)
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
    return render(request, 'bible_study.html', context)

def midweek_study(request):
    sermons = Sermon.objects.filter(categories='MIDWEEKSTUDY')
    paginator = Paginator(sermons, 4)
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
    return render(request, 'midweek_study.html', context)


def morning_devotion(request):
    sermons = Sermon.objects.filter(categories='MORNINGDEVOTION')
    paginator = Paginator(sermons, 4)
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
    return render(request, 'morning_devotion.html', context)


def sermon_detail(request, id):
    sermon = Sermon.objects.get(pk=id)
    latest = Sermon.objects.order_by('-timestamp')[:3]
    queryset = Sermon.objects.all()
    sermon_coments = sermon.message_set.all().order_by('-timestamp')

    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            sermon = sermon,
            content = request.POST.get('body')
        )

        return redirect(reverse("sermon-detail", kwargs={
                'id': sermon.pk
        }))
        
        # def get_success_url(self):
        #     return reverse("sermon-detail")
 

    context = {
        "sermon": sermon,
        "latest": latest,
        "queryset": queryset,
        "sermon_coments": sermon_coments
    }
    return render(request, "sermon_detail.html", context)


def event_detail(request, id):
    event = Event.objects.get(pk=id)
    context = {
        "event": event,
    }
    return render(request, "event_detail.html", context)




def sermon_create(request):
    title = 'CREATE'
    form = SermonForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("sermon-detail", kwargs={
                'id': form.instance.id
            }))

    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'sermon_create.html', context)

def sermon_update(request, id):
    title = 'UPDATE'
    sermon = get_object_or_404(Sermon, id=id)
    form = SermonForm(request.POST or None, request.FILES or None, instance=sermon)
    if request.method == "POST":
        if form.is_valid():
            form.save()

            return redirect(reverse("sermon-detail", kwargs={
                'id': form.instance.id
            }))

    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'sermon_create.html', context)

def sermon_delete(request, id):
    sermon = get_object_or_404(Sermon, id=id)
    sermon.delete()
    return redirect(reverse("sermons"))

def event_create(request):
    title = 'CREATE'
    form = EventForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("event-detail", kwargs={
                'id': form.instance.id
            }))

    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'event_create.html', context)


def event_update(request, id):
    title = 'UPDATE'
    event = get_object_or_404(Event, id=id)
    form = EventForm(request.POST or None, request.FILES or None, instance=event)
    if request.method == "POST":
        if form.is_valid():
            form.save()

            return redirect(reverse("event-detail", kwargs={
                'id': form.instance.id
            }))

    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'event_create.html', context)


def event_delete(request, id):
    event = get_object_or_404(Event, id=id)
    event.delete()
    return redirect(reverse("events"))
   

def aboutPage(request):
    return render(request, "about.html")

def contantPage(request):
    return render(request, "contact.html")

# def events(request):
#     events = Event.objects.filter(featured=True)
#     context = {
#         'object_list': events
#     }
#     return render(request, 'evtd.html', context)
