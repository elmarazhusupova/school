from django.urls import path
from .views import TeacherLoginView, TeacherRegistrationView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', TeacherLoginView.as_view(), name='login'),
    path('register/', TeacherRegistrationView.as_view(), name='register'),
]
