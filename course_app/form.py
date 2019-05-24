from . import models
from django import forms
from course_app.models import User


class FormName(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'
