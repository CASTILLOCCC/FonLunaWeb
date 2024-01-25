from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import asociados, aportes
from .forms import asociadosForm
from django.http import JsonResponse
from django.db.models import Q
from django.db.models import Sum
from .forms import AportesForm


#Asociados

def inicio(request):
    return render (request, 'paginas/inicio.html')

def aboutus(request):
    return render (request, 'paginas/aboutus.html')

def Asociados(request):
    aso = asociados.objects.all()
    return render (request, 'Asociados/index.html', {'asociadosView': aso})

def create(request):
    formulario = asociadosForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('Asociados')
    return render(request, 'Asociados/create.html', {'formulario': formulario})

def edit(request, id):
    asociado = asociados.objects.get(id=id)
    formulario = asociadosForm(request.POST or None, request.FILES or None, instance=asociado)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect(Asociados) 
    return render (request, 'Asociados/edit.html', {'formulario': formulario})


def eliminar(request, id):
    asociado = asociados.objects.get(id=id)
    asociado.delete()
    aso = asociados.objects.all()
    return render (request, 'Asociados/index.html', {'asociadosView': aso})

#Aportes

def Aportes(request):
    
    aportes_asociados = aportes.objects.select_related('idAsociado')  
    usuarios = aportes_asociados.values('idAsociado__Nombre').distinct()
    meses = aportes_asociados.values('MesAporte').distinct() 
    anos = aportes_asociados.values('AnoAporte').distinct()
    total_valor_aporte = 0
    total_intereses = 0
    total_devoluciones = 0
        

    if request.method == 'POST':
        MesUsuario = request.POST.get('mes_dropdown')
        NombreUsuario = request.POST.get('usuario_dropdown')
        AnoUsuario = request.POST.get('ano_dropdown')
        
        filters = Q()

        if MesUsuario:
            filters &= Q(MesAporte=MesUsuario)
        
        if NombreUsuario:
            filters &= Q(idAsociado__Nombre=NombreUsuario)
            
        if AnoUsuario:
            filters &= Q(AnoAporte=AnoUsuario)
        
        # Aplicamos los filtros a la consulta
        aportes_filtrados = aportes_asociados.filter(filters)
        
        total_valor_aporte = aportes_filtrados.aggregate(total=Sum('ValorAporte'))
        total_intereses = aportes_filtrados.aggregate(total=Sum('InteresAprote'))
        total_devoluciones = aportes_filtrados.aggregate(total=Sum('DevolAporte'))
        
        return render(request, 'Aportes/index.html', {
        'aportesView': aportes_filtrados,
        'usuarios': usuarios,
        'meses': meses,
        'anos': anos,
        'total_valor_aporte': total_valor_aporte['total'],
        'total_intereses': total_intereses['total'],
        'total_devoluciones': total_devoluciones['total'],
        })
        
    else:
        
        total_valor_aporte = aportes_asociados.aggregate(total=Sum('ValorAporte'))
        total_intereses = aportes_asociados.aggregate(total=Sum('InteresAprote'))
        total_devoluciones = aportes_asociados.aggregate(total=Sum('DevolAporte'))
        
        return render(request, 'Aportes/index.html', {
        'aportesView': aportes_asociados,
        'usuarios': usuarios,
        'meses': meses,
        'anos': anos,
        'total_valor_aporte': total_valor_aporte['total'],
        'total_intereses': total_intereses['total'],
        'total_devoluciones': total_devoluciones['total'],
        })

def create_aportes(request):
    
   if request.method == 'POST':
        # Crea una nueva instancia de aportes y asigna valores a sus campos
        nuevo_aporte = aportes()
        nuevo_aporte.idAsociado_id = request.POST.get('CodigoAsociado')
        nuevo_aporte.ValorAporte = request.POST.get('ValorAporte')
        nuevo_aporte.MesAporte = request.POST.get('Mes')
        nuevo_aporte.AnoAporte = request.POST.get('Ano')
        nuevo_aporte.InteresAprote = request.POST.get('interesAporte')
        nuevo_aporte.DevolAporte = request.POST.get('devolucionAportes')
        nuevo_aporte.FechaAporte = request.POST.get('fechaAportes')
        

        # Guarda la nueva instancia en la base de datos
        nuevo_aporte.save()

        return render(request, 'Aportes/index.html')
    

def edit_aportes(request, id):
    # Obtén el objeto de aportes que deseas editar
    aportes_edit = get_object_or_404(aportes, id=id)

    if request.method == 'POST':
        # Si se ha enviado un formulario POST, procesa los datos
        form = AportesForm(request.POST, instance=aportes_edit)
        if form.is_valid():
            form.save()
            return redirect('Aportes')  
    else:
        # Si es una solicitud GET, muestra el formulario de edición
        form = AportesForm(instance=aportes_edit)

    return render(request, 'Aportes/edit.html', {'form': form})



def search_asociados(request):
    term = request.GET.get('term')
    asociados = asociados.objects.filter(nombre__icontains=term).values('nombre')
    return JsonResponse(list(asociados), safe=False)


  
    