from django.urls import path
from .views import SignUpView, user_profile

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # ex: /users/5/
    path('<int:user_id>/', user_profile, name="profile")
]