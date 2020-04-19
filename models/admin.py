from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Comment, Event


class CustomUserAdmin(UserAdmin):
    model = User
    readonly_fields=('date_joined',)
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

admin.site.register(User, CustomUserAdmin)

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    #fields = ('date', 'comment')

admin.site.register(Comment, CommentAdmin)

class EventAdmin(admin.ModelAdmin):
    model = Event

admin.site.register(Event, EventAdmin)