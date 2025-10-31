from django.shortcuts import render
from .forms import ProduccionForm

def produccion_view(request):
    if request.method == 'POST':
        form = ProduccionForm(request.POST)
        if form.is_valid():
            # Procesar los datos del formulario
            horas_produccion = form.cleaned_data['horas_produccion'].split(',')
            tasa_produccion = form.cleaned_data['tasa_produccion'].split(',')
            target = form.cleaned_data['target'].split(',')
            costos_fijos = form.cleaned_data['costos_fijos'].split(',')
            costos_variables = form.cleaned_data['costos_variables'].split(',')
            # Aquí puedes agregar lógica adicional para manejar los datos
            return render(request, 'tienda/produccion_resultado.html', {
                'horas_produccion': horas_produccion,
                'tasa_produccion': tasa_produccion,
                'target': target,
                'costos_fijos': costos_fijos,
                'costos_variables': costos_variables,
            })
    else:
        form = ProduccionForm()

    return render(request, 'tienda/produccion_form.html', {'form': form})