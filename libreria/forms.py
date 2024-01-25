from django import forms
from .models import asociados
from .models import aportes

class asociadosForm(forms.ModelForm):
    class Meta:
        model = asociados
        fields = '__all__'
        
class MiFormulario(forms.Form):
    campo_dropdown = forms.ModelChoiceField(queryset=asociados.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    
class AportesForm(forms.ModelForm):
    class Meta:
        model = aportes
        fields = ['ValorAporte', 'MesAporte', 'AnoAporte', 'InteresAprote', 'DevolAporte', 'FechaAporte']