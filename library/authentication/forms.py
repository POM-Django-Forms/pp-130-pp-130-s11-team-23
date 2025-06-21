from django import forms
from .models import CustomUser

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'middle_name', 'role', 'password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Користувач з такою поштою вже існує.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm = cleaned_data.get('confirm_password')

        if password and confirm and password != confirm:
            self.add_error('confirm_password', "Паролі не співпадають.")