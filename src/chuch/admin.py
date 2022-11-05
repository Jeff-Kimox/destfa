from django.contrib import admin
from .models import User, Sermon, Event, Message

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'categories']
    list_filter = ['categories']

# Register your models here.
admin.site.register(User)
admin.site.register(Sermon)
admin.site.register(Message)
