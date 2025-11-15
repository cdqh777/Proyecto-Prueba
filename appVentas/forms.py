from django import forms
from .models import Cliente, Tienda

class ClienteForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    correo = forms.EmailField(label="Correo", required=True)

class TiendaForm(forms.Form):
    nombre = forms.CharField(label="Nombre de Tienda", max_length=100, required=True)
    direccion = forms.CharField(label="Dirección", max_length=150, required=True)

class CompraForm(forms.Form):
    fecha = forms.DateField(
        label="Fecha",
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    monto = forms.DecimalField(
        label="Monto",
        max_digits=10,
        decimal_places=2,
        required=True
    )
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        label="Cliente",
        required=True,
        empty_label="Seleccione un cliente"
    )
    tienda = forms.ModelChoiceField(
        queryset=Tienda.objects.all(),
        label="Tienda",
        required=True,
        empty_label="Seleccione una tienda"
    )
    
    def __init__(self, *args, **kwargs):
        super(CompraForm, self).__init__(*args, **kwargs)
        # Personalizar cómo se muestran los clientes y tiendas en el selector
        self.fields['cliente'].label_from_instance = lambda obj: f"{obj.id_cliente} - {obj.nombre}"
        self.fields['tienda'].label_from_instance = lambda obj: f"{obj.id_tienda} - {obj.nombre}"