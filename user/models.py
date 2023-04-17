from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.

class User(AbstractUser):
    # firstName = models.CharField(max_length=30,null=False)
    # email = models.EmailField(max_length=30)
    # password = models.CharField(max_length=30,null=False)
    is_developer = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_team_leader = models.BooleanField(default=False)
    is_tester = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'User'
