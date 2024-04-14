from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Users
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .forms import CsRegisterForm
from .forms import LoginForm
from django.views.generic import CreateView
from django.views.generic import FormView

#회원가입
class CsRegisterView(CreateView):
    model = Users
    template_name = 'accounts/signup.html'
    form_class = CsRegisterForm

    def get_success_url(self):
        messages.success(self.request, "회원가입 성공.")
        return redirect('/index/')

    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.get_success_url())



class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        user_id = form.cleaned_data.get("user_id")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=user_id, password=password)
        
        if user is not None:
            self.request.session['user_id'] = user_id
            login(self.request, user)

        return super().form_valid(form)   
    


def logout_view(request):
    logout(request)
    return redirect('/')

