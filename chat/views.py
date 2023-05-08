from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import *
from .forms import *

# Create your views here.
class IndexView(generic.edit.CreateView):
    template_name = 'chat/index.html'
    form_class = MessageForm
    success_url = reverse_lazy('chat:index')

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['objects'] = Message.objects.all()
       return context

    def form_valid(self, form):
        form.instance.user = self.request.user # Add the user to the form instance
        return super().form_valid(form)
