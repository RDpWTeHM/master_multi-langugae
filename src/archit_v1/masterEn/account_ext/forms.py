from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(label='密码')
    password2 = forms.CharField(label="重复输入密码")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('密码不匹配')
        return cd['password2']
