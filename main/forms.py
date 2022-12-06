from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db import models

class RegisterUser (UserCreationForm):
    class Meta:
        model= User
        fields =('first_name' ,'last_name', 'username', 'email', 'password1', 'password2')



class ImageUpload(ModelForm):
    img = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
