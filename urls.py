from django.urls import path

from . import views

urlpatterns = [
    path('', views.FrontPage.as_view(), name='frontpage'),
]