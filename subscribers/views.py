from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy

from .forms import SubscriberForm

# Create your views here.

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = SubscriberForm
    success_url = reverse_lazy('register_confirmation')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class RegisterConfirmationView(TemplateView):
    template_name = 'register_confirmation.html'