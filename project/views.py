from django.shortcuts import render,redirect
from .models import Project , ProjectTeam, ProjectModule, Task, UserTask, User
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView
from .forms import DashboardForm, TeamRegisterForm, ProjectModuleForm, TaskForm, UserTaskForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from user.decorators import manager_required,developer_required
from django.db.models import Q



# Create your views here.

def index(request):
    return render(request,'project/index.html')

def confirmMail(request):
    return render(request,'project/auth-confirm-mail.html')

@method_decorator([login_required(login_url='/login'),manager_required] , name='dispatch')
class Dashboard(CreateView):
    form_class = DashboardForm
    success_url = '/project/dashboard'
    template_name = 'project/page-project.html'

    def get_context_data(self, **kwargs):
        kwargs['project'] = Project.objects.all()
        return super(Dashboard, self).get_context_data(**kwargs)
    
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Project.objects.filter(
            Q(title__icontains=query)
        )
        return object_list
    
    # def get(self, request, *args, **kwargs):
    #     print("called....")
    #     input = request.GET.get('input')
    #     print(input)
    #     project=[]
    #     if input:
    #         project = Project.objects.filter(title__icontains=input)
    #         print(project)
    #         return render(request, self.template_name, {'project':project})
    #     else:
    #         project = Project.objects.all()    
    #         return render(request, self.template_name, {'project':project})

@method_decorator([login_required(login_url='/login'),manager_required] , name='dispatch')
class ProjectUpdate(UpdateView):
    model = Project
    form_class = DashboardForm
    template_name = 'project/project-update.html'
    success_url = '/project/dashboard'

class ProjectDetail(DetailView):
    model = Project
    template_name = 'project/project-detail.html'
    context_object_name = 'project'

    def get(self, request, *args, **kwargs):
        module = ProjectModule.objects.filter(project_id = self.kwargs['pk'])
        return render(request, self.template_name, {'project': self.get_object(),  'module' : module})

@method_decorator([login_required(login_url='/login'),manager_required] , name='dispatch')
class ProjectDelete(DeleteView):
    model = Project
    template_name = 'project/project-delete.html'
    success_url = '/project/dashboard'


# def projectAdd(request):
#      if  request.method=="POST":
#         model=Project()
#         model.name=request.POST['username']
#         model.email=request.POST.get("email")
#         model.password=request.POST['password']
#         model.recheckpassword=request.POST['repassword']
#         model.save()
#         return redirect('login')
#     return render(request,'signup.html')

@method_decorator([login_required(login_url='/login'),manager_required] , name='dispatch')
class TeamRegister(CreateView):
    form_class = TeamRegisterForm
    template_name = 'project/team-register.html'
    success_url = '/project/dashboard'


class TeamDetail(DetailView):
    model = ProjectTeam
    template_name = 'project/team-detail.html'
    context_object_name = 'projectdetail'

    def get(self, request, *args, **kwargs):
        team = ProjectTeam.objects.filter(project_id = self.kwargs['pk'])
        return render(request, self.template_name, {'projectdetail': self.get_object(), 'team': team})

@method_decorator([login_required(login_url='/login'),manager_required] , name='dispatch')
class TeamDelete(DeleteView):
    model = ProjectTeam
    template_name = 'project/team-delete.html'
    success_url = '/project/dashboard'

@method_decorator([login_required(login_url='/login'),manager_required] , name='dispatch')
class ProjectModuleCreate(CreateView):
    form_class = ProjectModuleForm
    template_name = 'project/project-module-create.html'
    success_url = '/project/'

class ProjectModuleDetail(DetailView):
    model = ProjectModule
    template_name = 'project/project-module-detail.html'
    context_object_name = 'project'

    def get(self, request, *args, **kwargs):
        task = Task.objects.filter(module_id = self.kwargs['pk'])
        user = UserTask.objects.all()
        return render(request, self.template_name, {'project': self.get_object(), 'task': task, 'user' : user})

@method_decorator([login_required(login_url='/login'),manager_required] , name='dispatch')
class ProjectModuleDelete(DeleteView):
    model = ProjectModule
    template_name = 'project/project-module-delete.html'
    success_url = '/project/dashboard'

@method_decorator([login_required(login_url='/login'),manager_required] , name='dispatch')
class ProjectModuleUpdate(UpdateView):
    model = ProjectModule
    form_class = ProjectModuleForm
    template_name = 'project/project-module-update.html'
    success_url = '/project/dashboard'

@method_decorator([login_required(login_url='/login'),manager_required] , name='dispatch')
class TaskCreate(CreateView):
    form_class = TaskForm
    template_name = 'project/task-create.html'
    success_url = '/project/'


class TaskDetail(DetailView):
    model = Task
    template_name = 'project/task-detail.html'
    context_object_name = 'project'

@method_decorator([login_required(login_url='/login'),manager_required] , name='dispatch')
class TaskDelete(DeleteView):
    model = Task
    template_name = 'project/task-delete.html'
    success_url = '/project/dashboard'

@method_decorator([login_required(login_url='/login'),manager_required] , name='dispatch')
class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'project/task-update.html'
    success_url = '/project/dashboard'

@method_decorator([login_required(login_url='/login'),manager_required] , name='dispatch')
class UserTaskView(CreateView):
    form_class = UserTaskForm
    template_name = 'project/user-task-assign.html'
    success_url = '/project/dashboard'

class ProjectTask(ListView):
    model = UserTask
    template_name = 'project/page-task.html'
    context_object_name = 'taskuser'

class ProjectIndexView(ListView):
    model = Project
    template_name = 'project/index.html'
    context_object_name = 'projects'

    def get(self, request, *args, **kwargs):
        task = Task.objects.count()
        user = User.objects.count()
        projects = Project.objects.all()
        project = Project.objects.count()
        module = ProjectModule.objects.count()
        return render(request, self.template_name, {'task': task, 'alluser' : user, 'projects' : projects , 'project' : project , 'module' : module})
    


class Desk(ListView):
    model = Task
    template_name = 'project/page-desk.html'
    context_object_name = 'alltask'

    def get(self, request, *args, **kwargs):
        active = Task.objects.filter( status_id = 1 ) 
        return render(request, self.template_name, {'active': active,'alltask' : Task.objects.all()})
    


