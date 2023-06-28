from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth import login, authenticate
from .forms import TeacherLoginForm, TeacherRegistrationForm
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'templates/index.html'


class TeacherLoginView(FormView):
    form_class = TeacherLoginForm
    template_name = 'login.html'

    def form_valid(self, form):
        phone_number = form.cleaned_data['phone_number']
        password = form.cleaned_data['password']
        user = authenticate(self.request, phone_number=phone_number, password=password)
        if user is not None:
            login(self.request, user)
            return redirect('student-list')
        else:
            return redirect('login')


class TeacherRegistrationView(FormView):
    form_class = TeacherRegistrationForm
    template_name = 'register.html'
    success_url = '/login/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
