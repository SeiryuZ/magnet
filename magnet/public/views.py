from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views import View
from django.shortcuts import render, redirect

from magnet.apps.users.forms import UserCreationForm, UserChangeForm
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
            messages.success(request, _("You have succcessfully registered. Please check your email for further instructions."))
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
            user = form.get_user()
            login(request, user)
            next_ = request.GET.get('next', None)
            if next_:
                return redirect(next_)
            else:
                return redirect('profile')
        return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class ProfileView(BaseFormView):
    form_class = UserChangeForm
    template_name = 'form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, _("Your profile has been updated"))
            return redirect('profile')
        return render(request, self.template_name, {'form': form})
