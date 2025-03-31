from django import forms

from users.models import User

class StyleFromMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(StyleFromMixin,forms.ModelForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Повторите Пароль", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password']:
            raise forms.ValidationError("Пароли не совпадают")
        return cd['password2']




class UserLoginForm(StyleFromMixin,forms.Form):
    email = forms.EmailField()
    password = forms.CharField(label="пароль", widget=forms.PasswordInput)


class UserForm(StyleFromMixin,forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone')
        # exclude = ('is_active,')
