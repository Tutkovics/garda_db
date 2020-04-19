from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

from .models import User, Comment, Event
from .forms import CustomUserCreationForm 

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@login_required
def user_profile(request, user_id):
    #return render(request, 'polls/index.html', context)
    #return HttpResponse("You're looking at user %s." % user_id)
    user = get_object_or_404(User, pk=user_id)
    # want to get own profile
    comments = None
    if request.user.id == user_id:
        comments = Comment.objects.filter(user_get=user_id)

    events = Event.objects.filter(orgaizers=user_id)
    return render(request, 'users/profile.html', {'user': user, 'comments': comments, 'events': events})