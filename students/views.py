from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Student
from django.shortcuts import render, redirect
from .forms import GradeForm, MessageForm
from django.http import HttpResponseNotFound, HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            student_email = form.cleaned_data['student_email']
            message = form.cleaned_data['message']
            html_message = render_to_string('email_template.html', {'message': message})
            send_mail('Contact Form', message, 'settings.EMAIL_HOST_USER', [student_email], html_message=html_message, fail_silently=False)
            return redirect('student_list')
    else:
        form = MessageForm()

    return render(request, 'send_email.html', {'form': form})


def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list.html')
    else:
        form = GradeForm()

    context = {'form': form}
    return render(request, 'add_grade.html', context)


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'

    def handle_no_permission(self):
        return HttpResponseNotFound('Access denied, please register or login')


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    template_name = 'student_create.html'
    fields = ['full_name', 'email', 'birth_date', 'grade', 'address', 'gender', 'image']
    success_url = reverse_lazy('student-list')

    def handle_no_permission(self):
        return HttpResponseNotFound('Access denied, please register or login')

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     subject = 'Добро пожаловать!'
    #     message = render_to_string('welcome_email.html', {'student': self.object})
    #     from_email = settings.DEFAULT_FROM_EMAIL
    #     recipient_list = [self.object.email]
    #
    #     send_mail(message, 'settings.EMAIL_HOST_USER', [])
    #
    #     return response


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = 'student_update.html'
    fields = ['full_name', 'email', 'birth_date', 'grade', 'address', 'gender', 'image']
    success_url = reverse_lazy('student-list')

    def handle_no_permission(self):
        return HttpResponseNotFound('Access denied, please register or login')


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'student_delete.html'
    success_url = reverse_lazy('student-list')

    def handle_no_permission(self):
        return HttpResponseNotFound('Access denied, please register or login')
