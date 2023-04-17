from django.db import models
from user.models import User    

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=30,null=False)
    description = models.CharField(max_length=500)
    technology = models.CharField(max_length=100)
    estimatedHours = models.PositiveIntegerField(max_length=9)
    startDate = models.DateField()
    completionDate = models.DateField()

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'Project'


class ProjectTeam(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ProjectTeam'

    def __str__(self):
        return str(self.project)

class Status(models.Model):
    statusName = models.CharField(max_length=20,unique=True,null=False)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.statusName

    class Meta:
        db_table = 'Status'

class ProjectModule(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,max_length=9)
    moduleName = models.CharField(max_length=30,null=False)
    description = models.CharField(max_length=30)
    estimatedHours = models.PositiveIntegerField()
    status = models.BooleanField(default=False)
    startDate = models.DateField()

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.moduleName
    
    class Meta:
        db_table = 'ProjectModule'

class Task(models.Model):
    module = models.ForeignKey(ProjectModule,on_delete=models.CASCADE,max_length=9)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,max_length=9)
    title = models.CharField(max_length=20)
    priority = models.CharField(max_length=30)
    description = models.CharField(max_length=500,null=False)
    status = models.ForeignKey(Status,on_delete=models.CASCADE,max_length=9)
    totalMinutes = models.PositiveIntegerField(max_length=9)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'Task'

class UserTask(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'UserTask'

    def __str__(self):
        return self.user.username
