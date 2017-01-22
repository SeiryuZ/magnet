from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect

from magnet.apps.users.forms import UserCreationForm
from .forms import LoginForm


class BaseFormView(View):

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})


class RegisterView(BaseFormView):
    form_class = UserCreationForm
    initial = {}
    template_name = 'form.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            messages.success(request, "Data anda telah terdaftarkan. Cek email anda untuk langkah lebih lanjut")
            form.save()
            return redirect('index')
        return render(request, self.template_name, {'form': form})


class LoginView(BaseFormView):
    form_class = LoginForm
    initial = {}
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request, data=request.POST)
        if form.is_valid():
            return redirect('profile')
        print(form.errors)
        return render(request, self.template_name, {'form': form})
