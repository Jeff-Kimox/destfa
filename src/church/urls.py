"""church URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from chuch import views
from chuch.views import RegisterView

from chuch.views import (
    index, events, sermons, sermon_detail,
    event_detail, login_page, logoutUser, youth_page,
    sermon_create, sermon_update, sermon_delete, event_create, aboutPage, contantPage,
    men_page, women_page, children_page, bible_study, midweek_study, morning_devotion,
    join_us, AppointmentTemplateView, ManageAppointmentTemplateView, my_donation_page,
    payment_succesful, payment_failed
    # event_create, event_update, event_delete

)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('join_us/', views.join_us, name="join-us"),
    path('register/', RegisterView.as_view(), name="register"),
    # path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('events/', views.events, name='events'),
    path('youth_page/', views.youth_page, name='youth-page'),
    path('men_page/', views.men_page, name='men-page'),
    path('women_page/', views.women_page, name='women-page'),
    path('children_page/', views.children_page, name='children-page'),
    path('bible_study/', views.bible_study, name='bible-study'),
    path('midweek_study/', views.midweek_study, name='midweek-study'),
    path('morning_devotion/', views.morning_devotion, name='morning-devotion'),
    path('sermons/', views.sermons, name='sermons'),
    path('sermon_create/', views.sermon_create, name='sermon-create'),
    path('event_create/', views.event_create, name='event-create'),
    path('sermon/<id>/', views.sermon_detail, name='sermon-detail'),
    path('sermon/<id>/update/', views.sermon_update, name='sermon-update'),
    path('sermon/<id>/delete/', views.sermon_delete, name='sermon-delete'),
    path('event/<id>/', views.event_detail, name='event-detail'),
    path('event/<id>/update/', views.event_update, name='event-update'),
    path('event/<id>/delete/', views.event_delete, name='event-delete'),
    path('about/', views.aboutPage, name='about'),
    path('contact/', views.contantPage, name='contact'),
    path("appointments/", AppointmentTemplateView.as_view(), name="appointment"),
    path("manage-appointments/", ManageAppointmentTemplateView.as_view(), name="manage-appointments"),
    path('tinymce/', include('tinymce.urls')),
    path('donate/', views.my_donation_page, name='donate'),
    path('payment_success/', views.payment_succesful, name='payment-succesful'),
    path('payment_failed/', views.payment_failed, name='payment-failed'),
]
   



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
