from django import forms
from django.forms import widgets
from dept.models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        # fields = ('fname','lname','age','std_track','is_graduated')
        fields = '__all__'
        widgets={
            'fname':forms.TextInput(attrs={'class':'form-control'}),
            'lname':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            'std_track':forms.Select(attrs={'class':'form-control'}),
        }

class TrackForm(forms.ModelForm):
    class Meta:
        model= Track
        # fields = ('name',)
        fields = '__all__'
