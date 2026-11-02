from django.db import models
from django.contrib.auth.models import User

class Productor(models.Model):
    """Modelo para almacenar información de productores"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='productor')
    nombre = models.CharField(max_length=200)
    nit = models.CharField(max_length=20, unique=True)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Productor'
        verbose_name_plural = 'Productores'
    
    def __str__(self):
        return f"{self.nombre} - {self.nit}"


class Producto(models.Model):
    """Modelo para los productos agrícolas"""
    TIPO_CHOICES = [
        ('CAFE', 'Café'),
        ('FLORES', 'Flores'),
        ('AGUACATE', 'Aguacate'),
    ]
    
    productor = models.ForeignKey(Productor, on_delete=models.CASCADE, related_name='productos')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    nombre = models.CharField(max_length=200)
    nombre_finca = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=300)
    caracteristicas = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    unidad = models.CharField(max_length=50, default='kg')
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-fecha_publicacion']
    
    def __str__(self):
        return f"{self.nombre} - {self.nombre_finca}"


class Normativa(models.Model):
    """Modelo para almacenar normatividad de exportación"""
    TIPO_PRODUCTO_CHOICES = [
        ('CAFE', 'Café'),
        ('FLORES', 'Flores'),
        ('AGUACATE', 'Aguacate'),
    ]
    
    tipo_producto = models.CharField(max_length=20, choices=TIPO_PRODUCTO_CHOICES)
    titulo = models.CharField(max_length=300)
    descripcion = models.TextField()
    requisitos = models.TextField()
    documentacion = models.TextField()
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Normativa'
        verbose_name_plural = 'Normativas'
    
    def __str__(self):
        return f"{self.get_tipo_producto_display()} - {self.titulo}"


class PrecioMercado(models.Model):
    """Modelo para precios promedio del mercado"""
    TIPO_PRODUCTO_CHOICES = [
        ('CAFE', 'Café'),
        ('FLORES', 'Flores'),
        ('AGUACATE', 'Aguacate'),
    ]
    
    tipo_producto = models.CharField(max_length=20, choices=TIPO_PRODUCTO_CHOICES)
    precio_promedio = models.DecimalField(max_digits=10, decimal_places=2)
    unidad = models.CharField(max_length=50, default='kg')
    fecha = models.DateField(auto_now=True)
    fuente = models.CharField(max_length=200, blank=True)
    
    class Meta:
        verbose_name = 'Precio de Mercado'
        verbose_name_plural = 'Precios de Mercado'
        ordering = ['-fecha']
    
    def __str__(self):
        return f"{self.get_tipo_producto_display()} - ${self.precio_promedio} por {self.unidad}"


class Noticia(models.Model):
    """Modelo para noticias sobre exportaciones"""
    titulo = models.CharField(max_length=300)
    resumen = models.TextField()
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='noticias/', null=True, blank=True)
    fuente = models.CharField(max_length=200, blank=True)
    url_externa = models.URLField(blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
        ordering = ['-fecha_publicacion']
    
    def __str__(self):
        return self.titulo


class TRM(models.Model):
    """Modelo para almacenar la Tasa Representativa del Mercado"""
    fecha = models.DateField(unique=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = 'TRM'
        verbose_name_plural = 'TRM'
        ordering = ['-fecha']
    
    def __str__(self):
        return f"TRM {self.fecha}: ${self.valor}"
