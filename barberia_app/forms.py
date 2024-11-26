from django import forms
from .models import Formulario, Servicio

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['nombre_cliente', 'correo', 'dia_hora', 'servicios']

    # Validación personalizada si se requiere
    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        # Aquí podemos agregar validación de formato si lo necesitas
        if not correo:
            raise forms.ValidationError('Este campo es obligatorio.')
        return correo
