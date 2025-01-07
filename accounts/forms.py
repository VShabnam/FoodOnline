from django import forms
from .models import User

class UserForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput())
    confirm_password= forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model= User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def clean(self):
        cleanded_data = super(UserForm, self).clean()
        password = cleanded_data.get('password')
        confirm_password = cleanded_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        
               
  

