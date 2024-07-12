from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, ButtonHolder
from django import forms
from django.contrib.auth.forms import UserCreationForm
from usuarios.models import CustomUser

class RegistroForm(UserCreationForm):
    nombres = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellidos = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    correo = forms.EmailField(max_length=100, required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    num_doc_identificacion = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'nombres', 'apellidos', 'num_doc_identificacion', 'correo', 'telefono', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.first_name = self.cleaned_data['nombres']
        user.last_name = self.cleaned_data['apellidos']
        user.email = self.cleaned_data['correo']
        user.num_doc_identificacion = self.cleaned_data['num_doc_identificacion']
        user.telefono = self.cleaned_data['telefono']
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                'username',
                'nombres',
                'apellidos',
                'num_doc_identificacion',
                'correo',
                'telefono',
                'password1',
                'password2',
                css_class='form-group'
            ),
            ButtonHolder(
                Submit('submit', 'Registrarse', css_class='btn btn-primary')
            )
        )