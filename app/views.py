from django.shortcuts import render, redirect
from .forms import VentaForm

def registrar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venta_exitosa')
    else:
        form = VentaForm()
    return render(request, 'app/venta.html', {'form': form})


def venta_exitosa(request):
    return render(request, 'app/venta_exitosa.html')

