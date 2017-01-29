from django.conf.urls import url

from .views import RegisterView, LoginView, ProfileView, LogoutView, ChangePasswordView, HomeView

urlpatterns = [
    url(r'register$', RegisterView.as_view(), name='register'),
    url(r'profile$', ProfileView.as_view(), name='profile'),
    url(r'login', LoginView.as_view(), name='login'),
    url(r'logout', LogoutView.as_view(), name='logout'),
    url(r'change-password', ChangePasswordView.as_view(), name='change-password'),
    url(r'home', HomeView.as_view(), name='home'),
    url(r'^$', LoginView.as_view(), name='login'),
]
