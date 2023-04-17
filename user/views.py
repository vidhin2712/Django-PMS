from django.shortcuts import render
from .models import User
from django.views.generic.edit import CreateView
from .forms import ManagerRegisterForm,DeveloperRegisterForm,TeamLeaderRegisterForm,TesterRegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .forms import MyAuthForm


# Create your views here.

class ManagerRegisterView(CreateView):
    model = User
    form_class = ManagerRegisterForm
    template_name = 'user/manager_register.html'
    success_url = "/project/login"

    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)

class DeveloperRegisterView(CreateView):
    model = User
    form_class = DeveloperRegisterForm
    template_name = 'user/developer_register.html'
    success_url = "/project/login"

class TeamLeadeRegisterView(CreateView):
    model = User
    form_class = TeamLeaderRegisterForm
    template_name = 'user/team_leader_register.html'
    success_url = "/project/login"

class TesterRegisterView(CreateView):
    model = User
    form_class = TesterRegisterForm
    template_name = 'user/tester_register.html'
    success_url = "/project/login"

class SignUp(CreateView):
    model = User
    form_class = TesterRegisterForm
    template_name = 'user/signup.html'
    success_url = "/project/login"



class UserLogin(LoginView):
    template_name = 'user/login.html'
    authentication_form= MyAuthForm

    def get_redirect_url(self):
        if self.request.user.is_authenticated: 
            
            if self.request.user.is_manager:
                return '/project/dashboard'
        
            elif self.request.user.is_developer:
                return '/project/index'
        
            elif self.request.user.is_tester:
                return '/project/index'

            else:
                return '/project/index'
    
def temp(request):
    return render(request , 'project/chart-apex.html')






