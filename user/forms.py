from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User
from crispy_forms.helper import FormHelper
from django.contrib.auth.forms import AuthenticationForm

class ManagerRegisterForm(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'password' }),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'Confirm password'}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username' , 'email' , 'password1' , 'password2')

        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'First Name' , 'style': 'margin-top: 20px; margin-bottom: 20px;'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control' , 'placeholder' : 'Email' , 'style': 'margin-top: 20px; margin-bottom: 20px;'}),
            # 'password1' : forms.PasswordInput(attrs={'class' : 'form-control' , 'placeholder' : 'Password'}),
            # 'password2' : forms.PasswordInput(attrs={'class' : 'form-control' , 'placeholder' : 'RE Password'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(ManagerRegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    @transaction.atomic
    def save(self): 
        user = super().save(commit=False)
        user.is_manager = True
        user.save()
        return user
    
class DeveloperRegisterForm(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'password' , 'style': 'margin-top: 20px; margin-bottom: 20px;'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'Confirm password' , 'style': 'margin-top: 20px; margin-bottom: 20px;'}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username' , 'email' , 'password1' , 'password2')

        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'First Name' , 'style': 'margin-top: 20px; margin-bottom: 20px;'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control' , 'placeholder' : 'Email' , 'style': 'margin-top: 20px; margin-bottom: 20px;'}),
            # 'password1' : forms.PasswordInput(attrs={'class' : 'form-control' , 'placeholder' : 'Password'}),
            # 'password2' : forms.PasswordInput(attrs={'class' : 'form-control' , 'placeholder' : 'RE Password'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(DeveloperRegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_developer = True
        user.save()
        return user
    
class TeamLeaderRegisterForm(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'password' , 'style': 'margin-top: 20px; margin-bottom: 20px;'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'Confirm password' , 'style': 'margin-top: 20px; margin-bottom: 20px;'}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username' , 'email' , 'password1' , 'password2')

        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'First Name' , 'style': 'margin-top: 20px; margin-bottom: 20px;'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control' , 'placeholder' : 'Email' , 'style': 'margin-top: 20px; margin-bottom: 20px;'}),
            # 'password1' : forms.PasswordInput(attrs={'class' : 'form-control' , 'placeholder' : 'Password'}),
            # 'password2' : forms.PasswordInput(attrs={'class' : 'form-control' , 'placeholder' : 'RE Password'}),
        }

    def __init__(self, *args, **kwargs):
        super(TeamLeaderRegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_team_leader = True
        user.save()
        return user
    
class TesterRegisterForm(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'password' , 'style': 'margin-top: 20px; margin-bottom: 20px;'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'Confirm password' , 'style': 'margin-top: 20px; margin-bottom: 20px;'}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username' , 'email' , 'password1' , 'password2')

        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'First Name' , 'style': 'margin-top: 20px; margin-bottom: 20px;'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control' , 'placeholder' : 'Email' , 'style': 'margin-top: 20px; margin-bottom: 20px;'}),
            # 'password1' : forms.PasswordInput(attrs={'class' : 'form-control' , 'placeholder' : 'Password'}),
            # 'password2' : forms.PasswordInput(attrs={'class' : 'form-control' , 'placeholder' : 'RE Password'}),
        }

    def __init__(self, *args, **kwargs):
        super(TesterRegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_tester = True
        user.save()
        return user
    
class SignUp(UserCreationForm):
    
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'Confirm password'}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username' , 'email' , 'password1' , 'password2')

        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'First Name' , 'style': 'margin-top: 20px; margin-bottom: 20px;'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control' , 'placeholder' : 'Email' , 'style': 'margin-top: 20px; margin-bottom: 20px;'}),
            # 'password1' : forms.PasswordInput(attrs={'class' : 'form-control' , 'placeholder' : 'Password'}),
            # 'password2' : forms.PasswordInput(attrs={'class' : 'form-control' , 'placeholder' : 'RE Password'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(SignUp, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_tester = True
        user.save()
        return user
    
class MyAuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']
    
    def __init__(self, *args, **kwargs):
        super(MyAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        self.fields['username'].label = False
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}) 
        self.fields['password'].label = False

    