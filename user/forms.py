from django import forms
from .models import CustomUser
from  django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name' , 'year' , 'password']

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and len(password) < 8:
            raise ValidationError("Parol juda qisqa! Kamida 8 ta belgi bo'lishi kerak.")

        if password and password.isdigit():
            raise ValidationError("Parol faqat raqamlardan iborat bo'la olmaydi!")

        if username and password and username.lower() == password.lower():
            raise ValidationError("Foydalanuvchi nomi va parol bir xil bo'lishi mumkin emas!")

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Kiritilgan parollar bir-biriga mos kelmadi!")

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user is None:
                raise ValidationError("Foydalanuvchi nomi yoki parol noto'g'ri!")

        return cleaned_data