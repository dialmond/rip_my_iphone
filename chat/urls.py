from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = 'chat'
urlpatterns = [
    path('', RedirectView.as_view(url='chat/')),
    path('chat/', views.IndexView.as_view(), name='index'),
]
