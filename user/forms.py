from django import forms
from django.contrib.auth.forms import UsernameField
from .models import Teacher


class TeacherLoginForm(forms.Form):
    phone_number = forms.CharField(
        label='Номер телефона',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    field_order = ['phone_number', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        phone_number = cleaned_data.get('phone_number')
        password = cleaned_data.get('password')
        if phone_number and password:
            user = Teacher.objects.filter(phone_number=phone_number).first()
            if user is None or not user.check_password(password):
                self.add_error('phone_number', 'Неверный номер телефона или пароль.')
        return cleaned_data


class TeacherRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    confirm_password = forms.CharField(
        label='Подтвердите пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Teacher
        fields = ['phone_number']
        labels = {'phone_number': 'Номер телефона'}
        widgets = {'phone_number': forms.TextInput(attrs={'class': 'form-control'})}

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают.')
        return confirm_password

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        user.set_password(password)
        if commit:
            user.save()
        return user