from django.urls import path
from . import views
from users import views as register

urlpatterns = [
    path('register/', register.register, name='register'),
]
