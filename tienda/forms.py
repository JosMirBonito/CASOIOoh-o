from django import forms

class ProduccionForm(forms.Form):
    horas_produccion = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Ingrese las horas de producción separadas por comas'}), label='Horas de Producción')
    tasa_produccion = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Ingrese las tasas de producción separadas por comas'}), label='Tasa de Producción')
    target = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Ingrese los targets separados por comas'}), label='Target')
    costos_fijos = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Ingrese los costos fijos separados por comas'}), label='Costos Fijos')
    costos_variables = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Ingrese los costos variables separados por comas'}), label='Costos Variables')