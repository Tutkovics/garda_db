from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


# class UserManager(BaseUserManager):

#   def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
#     if not email:
#         raise ValueError('Users must have an email address')
#     now = timezone.now()
#     email = self.normalize_email(email)
#     user = self.model(
#         email=email,
#         is_staff=is_staff, 
#         is_active=True,
#         is_superuser=is_superuser, 
#         last_login=now,
#         date_joined=now, 
#         **extra_fields
#     )
#     user.set_password(password)
#     user.save(using=self._db)
#     return user

#   def create_user(self, email, password, **extra_fields):
#     return self._create_user(email, password, False, False, **extra_fields)

#   def create_superuser(self, email, password, **extra_fields):
#     user=self._create_user(email, password, True, True, **extra_fields)
#     user.save(using=self._db)
#     return user


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True)
    nick_name = models.CharField(max_length=254, null=True)
    is_staff = models.BooleanField(default=False)  # free to use
    is_superuser = models.BooleanField(default=False)  # god
    is_active = models.BooleanField(default=True)  # active user can log in
    last_login = models.DateTimeField(null=True, blank=True)
    date_hired = models.DateTimeField(null=True)  # date when the SSSL hired
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    # objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)


    def __str__(self):
        if not self.nick_name:
            return self.email
        else:
            return self.nick_name


class Comment(models.Model):
    date =  models.DateTimeField(null=True)
    event = models.ForeignKey(
        'models.Event',
        on_delete=models.CASCADE,
        null=True
    ) 
    user_get = models.ForeignKey(
        'models.User',
        on_delete=models.CASCADE,
    )
    #user_add = models.ManyToManyField(User)
    user_add = models.ForeignKey(
        'models.User',
        related_name='comment_added_by',
        on_delete=models.CASCADE,
    )
    comment = models.TextField(null=True, blank=True)


    def __str__(self):
        return " - ".join({str(self.user_get), str(self.date.year)})

class Event(models.Model):
    date =  models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=254, null=True, blank=True)
    # organizer = models.ForeignKey(
    #     'users.User',
    #     on_delete=models.CASCADE,
    # )
    orgaizers = models.ManyToManyField(User)
    note = models.TextField(null=True, blank=True)  # random notes connected to this event

    @property
    def year(self):
        "Return the year of the event."
        if not self.date:
            return "---"
        return self.date.year

    def __str__(self):
        # format: [EVENT.TITLE] - [EVENT.YEAR]
        return " - ".join({self.title, str(self.year)})