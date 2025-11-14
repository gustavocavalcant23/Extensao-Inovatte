from django.views.generic import FormView, TemplateView

from contacts.forms import UserContactForm


class HomeView(FormView):
    template_name = 'home.html'
    form_class = UserContactForm
    success_url = 'confirmation'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class ConfirmationView(TemplateView):
    template_name = 'confirmation.html'



