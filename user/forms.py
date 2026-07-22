from django import forms
from .models import CustomUser
from  django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name' , 'year' , 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        username = self.cleaned_data.get('username')  # Login bilan solishtirish uchun

        if password and len(password) < 8:
            raise ValidationError("Parol juda qisqa! Kamida 8 ta belgi bo'lishi kerak.")

        if username and password and username.lower() == password.lower():
            raise ValidationError("Foydalanuvchi nomi va parol bir xil bo'lishi mumkin emas!")

        if password and password.isdigit():
            raise ValidationError("Parol faqat raqamlardan iborat bo'la olmaydi!")

        return password

    def clean(self):
        data = super().clean()
        username = data.get('username')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password and confirm_password and  password != confirm_password:
            raise ValidationError("Passwords mos emas !! ")

        if username and password and username.lower() == password.lower():
            raise ValidationError(
                 "Foydalanuvchi nomi va parol bir xil bo'lishi mumkin emas!"
            )
        return data
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)