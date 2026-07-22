from django.urls import path
from .views import home, RegisterView , LoginView

urlpatterns = [
    path('reg/', RegisterView.as_view() , name='register'),
    path('home/' , home , name='home'),
    path('login/', LoginView.as_view() , name='login'),
]