from django.views import View
from django.shortcuts import render, redirect

from magnet.apps.users.forms import UserCreationForm


class RegisterView(View):
    form_class = UserCreationForm
    initial = {}
    template_name = 'form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request, 'index')
        return render(request, self.template_name, {'form': form})
