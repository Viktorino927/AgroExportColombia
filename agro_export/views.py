from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from datetime import date
from agro_export.models import Productor, Producto, Normativa, PrecioMercado, Noticia, TRM
from config.forms import RegistroProductorForm, ProductoForm


def home(request):
    """Vista principal del sitio"""
    # Obtener noticias recientes
    noticias = Noticia.objects.filter(activa=True)[:6]
    
    # Obtener TRM del día
    try:
        trm_hoy = TRM.objects.filter(fecha=date.today()).first()
    except:
        trm_hoy = None
    
    # Obtener precios promedio
    precios_mercado = PrecioMercado.objects.all()[:3]
    
    # Productos con mejor precio (los más económicos)
    productos_destacados = Producto.objects.filter(activo=True).order_by('precio')[:6]
    
    context = {
        'noticias': noticias,
        'trm': trm_hoy,
        'precios_mercado': precios_mercado,
        'productos_destacados': productos_destacados,
    }
    return render(request, 'home.html', context)


def normatividad(request):
    """Vista de normatividad y requisitos de exportación"""
    normativas_cafe = Normativa.objects.filter(tipo_producto='CAFE')
    normativas_flores = Normativa.objects.filter(tipo_producto='FLORES')
    normativas_aguacate = Normativa.objects.filter(tipo_producto='AGUACATE')
    
    context = {
        'normativas_cafe': normativas_cafe,
        'normativas_flores': normativas_flores,
        'normativas_aguacate': normativas_aguacate,
    }
    return render(request, 'normatividad.html', context)


def productos(request):
    """Vista de productos disponibles"""
    tipo_filtro = request.GET.get('tipo', None)
    
    if tipo_filtro:
        productos = Producto.objects.filter(activo=True, tipo=tipo_filtro)
    else:
        productos = Producto.objects.filter(activo=True)
    
    # Separar por tipo
    productos_cafe = productos.filter(tipo='CAFE')
    productos_flores = productos.filter(tipo='FLORES')
    productos_aguacate = productos.filter(tipo='AGUACATE')
    
    context = {
        'productos_cafe': productos_cafe,
        'productos_flores': productos_flores,
        'productos_aguacate': productos_aguacate,
        'tipo_filtro': tipo_filtro,
    }
    return render(request, 'productos.html', context)


def usuarios_view(request):
    """Vista de gestión de usuarios"""
    if request.user.is_authenticated:
        return redirect('perfil_productor')
    return render(request, 'usuarios.html')


def registro(request):
    """Vista de registro de nuevos productores"""
    if request.method == 'POST':
        form = RegistroProductorForm(request.POST)
        if form.is_valid():
            # Crear usuario
            user = form.save()
            
            # Crear perfil de productor
            Productor.objects.create(
                user=user,
                nombre=form.cleaned_data['nombre'],
                nit=form.cleaned_data['nit'],
                direccion=form.cleaned_data['direccion'],
                telefono=form.cleaned_data['telefono'],
                email=form.cleaned_data['email']
            )
            
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = RegistroProductorForm()
    
    return render(request, 'registro.html', {'form': form})


def login_view(request):
    """Vista de inicio de sesión"""
   
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'¡Bienvenido {user.username}!')
            next_page = request.GET.get('next')
            allowed_pages = ['home', 'dashboard', 'perfil']
            if next_page not in allowed_pages:
            next_page = 'home'
            return redirect(next_page)
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    
    return render(request, 'login.html')


def logout_view(request):
    """Vista de cierre de sesión"""
    logout(request)
    messages.info(request, 'Has cerrado sesión exitosamente.')
    return redirect('home')


@login_required
def perfil_productor(request):
    """Vista de perfil del productor"""
    try:
        productor = request.user.productor
        productos = productor.productos.all()
        
        context = {
            'productor': productor,
            'productos': productos,
        }
        return render(request, 'perfil_productor.html', context)
    except:
        messages.error(request, 'No tienes un perfil de productor asociado.')
        return redirect('home')


#@login_required
def agregar_producto(request):
    """Vista para agregar un nuevo producto"""
    try:
        productor = request.user.productor
    except:
        messages.error(request, 'Debes ser un productor para agregar productos.')
        # return redirect('home')
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.productor = productor
            producto.save()
            messages.success(request, '¡Producto agregado exitosamente!')
            return redirect('perfil_productor')
    else:
        form = ProductoForm()
    
    return render(request, 'agregar_producto.html', {'form': form})


@login_required
def editar_producto(request, producto_id):
    """Vista para editar un producto existente"""
    try:
        productor = request.user.productor
        producto = get_object_or_404(Producto, id=producto_id, productor=productor)
    except:
        messages.error(request, 'No tienes permiso para editar este producto.')
        return redirect('home')
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Producto actualizado exitosamente!')
            return redirect('perfil_productor')
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})


@login_required
def eliminar_producto(request, producto_id):
    """Vista para eliminar un producto"""
    try:
        productor = request.user.productor
        producto = get_object_or_404(Producto, id=producto_id, productor=productor)
        producto.activo = False
        producto.save()
        messages.success(request, 'Producto eliminado exitosamente.')
    except:
        messages.error(request, 'No tienes permiso para eliminar este producto.')
    
    return redirect('perfil_productor')
