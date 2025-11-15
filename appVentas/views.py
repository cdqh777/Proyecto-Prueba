from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Cliente, Tienda, Compra
from .forms import ClienteForm, TiendaForm, CompraForm

def pagina_inicial(request):
    """Página de presentación del proyecto"""
    return render(request, 'pagina_inicial.html')

# ==================== AUTENTICACIÓN ====================
def login_view(request):
    """Vista de login"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_clientes')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')

def logout_view(request):
    """Vista de logout"""
    logout(request)
    return redirect('pagina_inicial')

# ==================== CLIENTES ====================
@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})

@login_required
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            Cliente.objects.create(
               nombre = form.cleaned_data['nombre'],
               email = form.cleaned_data['correo'] 
            )
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'nuevo_cliente.html',{'form': form})

@login_required
def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente = id)
    cliente.delete()
    return redirect('lista_clientes')

@login_required
def actualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente = id)
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente.nombre = form.cleaned_data['nombre']
            cliente.email = form.cleaned_data['correo']
            cliente.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(initial={
            'nombre': cliente.nombre,
            'correo': cliente.email,
        })
    return render(request, 'actualizar_cliente.html', {'form':form})

# ==================== TIENDAS ====================
@login_required
def lista_tiendas(request):
    tiendas = Tienda.objects.all()
    return render(request, 'listar_tiendas.html', {'tiendas': tiendas})

@login_required
def crear_tienda(request):
    if request.method == 'POST':
        form = TiendaForm(request.POST)
        if form.is_valid():
            Tienda.objects.create(
                nombre=form.cleaned_data['nombre'],
                direccion=form.cleaned_data['direccion']
            )
            return redirect('lista_tiendas')
    else:
        form = TiendaForm()
    return render(request, 'nueva_tienda.html', {'form': form})

@login_required
def eliminar_tienda(request, id):
    tienda = get_object_or_404(Tienda, id_tienda=id)
    tienda.delete()
    return redirect('lista_tiendas')

@login_required
def actualizar_tienda(request, id):
    tienda = get_object_or_404(Tienda, id_tienda=id)
    if request.method == 'POST':
        form = TiendaForm(request.POST)
        if form.is_valid():
            tienda.nombre = form.cleaned_data['nombre']
            tienda.direccion = form.cleaned_data['direccion']
            tienda.save()
            return redirect('lista_tiendas')
    else:
        form = TiendaForm(initial={
            'nombre': tienda.nombre,
            'direccion': tienda.direccion,
        })
    return render(request, 'actualizar_tienda.html', {'form': form})

# ==================== COMPRAS ====================
@login_required
def lista_compras(request):
    compras = Compra.objects.all().select_related('cliente', 'tienda')
    return render(request, 'listar_compras.html', {'compras': compras})

@login_required
def crear_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            Compra.objects.create(
                fecha=form.cleaned_data['fecha'],
                monto=form.cleaned_data['monto'],
                cliente=form.cleaned_data['cliente'],
                tienda=form.cleaned_data['tienda']
            )
            return redirect('lista_compras')
    else:
        form = CompraForm()
    return render(request, 'nueva_compra.html', {'form': form})

@login_required
def eliminar_compra(request, id):
    compra = get_object_or_404(Compra, id_compra=id)
    compra.delete()
    return redirect('lista_compras')

@login_required
def actualizar_compra(request, id):
    compra = get_object_or_404(Compra, id_compra=id)
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra.fecha = form.cleaned_data['fecha']
            compra.monto = form.cleaned_data['monto']
            compra.cliente = form.cleaned_data['cliente']
            compra.tienda = form.cleaned_data['tienda']
            compra.save()
            return redirect('lista_compras')
    else:
        form = CompraForm(initial={
            'fecha': compra.fecha,
            'monto': compra.monto,
            'cliente': compra.cliente,
            'tienda': compra.tienda,
        })
    return render(request, 'actualizar_compra.html', {'form': form})