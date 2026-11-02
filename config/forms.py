from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from agro_export.models import  Producto


class RegistroProductorForm(UserCreationForm):
    """Formulario para registro de nuevos productores"""
    nombre = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'})
    )
    nit = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NIT'})
    )
    direccion = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Dirección', 'rows': 3})
    )
    telefono = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'})
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contraseña'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirmar contraseña'})


class ProductoForm(forms.ModelForm):
    """Formulario para crear/editar productos"""
    class Meta:
        model = Producto
        fields = ['tipo', 'nombre', 'nombre_finca', 'ubicacion', 'caracteristicas', 'precio', 'unidad', 'imagen']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'nombre_finca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la finca'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ubicación'}),
            'caracteristicas': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Características del producto', 'rows': 4}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
            'unidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unidad (ej: kg, lb)'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'tipo': 'Tipo de Producto',
            'nombre': 'Nombre del Producto',
            'nombre_finca': 'Nombre de la Finca',
            'ubicacion': 'Ubicación',
            'caracteristicas': 'Características',
            'precio': 'Precio',
            'unidad': 'Unidad',
            'imagen': 'Imagen del Producto',
        }
