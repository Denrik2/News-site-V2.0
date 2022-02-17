from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse


def account(request):
    return render(request, 'account/account_main.html')


class LoginView(TemplateView):
    template_name = 'account/account_user.html'

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("profile"))
            else:
                context['error'] = 'Логин или пароль неправильные'
        return render(request, self.template_name, context)


class ProfilePage(TemplateView):
    template_name = 'account/account_profile.html'


class RegisterView(TemplateView):
    template_name = "account/account_register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect(reverse("login"))

        return render(request, self.template_name)