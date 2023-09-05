from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from .validations import validate_length

class CustomUser(AbstractUser):
    contact = models.PositiveIntegerField(validators = [validate_length,MaxValueValidator(9999999999)], null=True, blank =True)
    
    def __str__(self):
        return self.username
    
