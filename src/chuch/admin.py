from django.contrib import admin
from .models import User, Sermon, Category, Event

# Register your models here.
admin.site.register(User)
admin.site.register(Sermon)
admin.site.register(Category)
admin.site.register(Event)
