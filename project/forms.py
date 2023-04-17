from django import forms
from .models import Project, ProjectTeam, ProjectModule, Task, UserTask


class DashboardForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
    
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'project Title'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control' , 'placeholder' : 'Enter Description here' , 'rows' : 2 }),
            'technology' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Enter Technlogy'}),
            'estimatedHours' : forms.NumberInput(attrs={'class' : 'form-control' , 'placeholder' : 'Enter Estimated Hours'}),
            'startDate' : forms.DateInput(attrs={'class' : 'form-control' , 'placeholder' : 'mm/dd/yyyy'}),
            'completionDate' : forms.DateInput(attrs={'class' : 'form-control' , 'placeholder' : 'mm/dd/yyyy'}),
        }
class TeamRegisterForm(forms.ModelForm):
    class Meta: 
        model = ProjectTeam
        fields = '__all__'
    
        widgets = {
            'project' : forms.Select(attrs={'class' : 'form-control' , 'style' : 'margin-bottom : 20px', 'placeholder' : 'Select Project'}),
            'user' : forms.Select(attrs={'class' : 'form-control' , 'style' : 'margin-bottom : 20px' }),
        }

class ProjectModuleForm(forms.ModelForm):

    status : forms.BooleanField(required=True)

    class Meta:
        model = ProjectModule
        fields = '__all__'
    
        widgets = {
            'project' : forms.Select(attrs={'class' : 'form-control'}),
            'moduleName' : forms.TextInput(attrs={'class' : 'form-control'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control', 'rows' : 2}),
            'estimatedHours' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'startDate' : forms.DateInput(attrs={'class' : 'form-control'}),
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'project' : forms.Select(attrs={'class' : 'form-control'}),
            'module' : forms.Select(attrs={'class' : 'form-control'}),
            'priority' : forms.TextInput(attrs={'class' : 'form-control'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control', 'rows' : 3}),
            'status' : forms.Select(attrs={'class' : 'form-control'}),
            'totalMinutes' : forms.NumberInput(attrs={'class' : 'form-control'}),
        }

class UserTaskForm(forms.ModelForm):
    class Meta:
        model = UserTask
        fields = '__all__'

        widgets = {
            'task' : forms.Select(attrs={'class' : 'form-control'}),
            'user' : forms.Select(attrs={'class' : 'form-control'}),
        }