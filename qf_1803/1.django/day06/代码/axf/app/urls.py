
from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^home/', views.Home, name='home'),
]

