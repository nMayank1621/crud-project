from django import forms
from .models import Student 

class AddStudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ("name", "roll", "city", "email", "phone_number")

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'roll': forms.NumberInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control'}),
        }