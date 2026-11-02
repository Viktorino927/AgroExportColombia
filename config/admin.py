from django.contrib import admin
from ..agro_export.models import Productor, Producto, Normativa, PrecioMercado, Noticia, TRM


@admin.register(Productor)
class ProductorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'nit', 'telefono', 'email', 'fecha_registro']
    search_fields = ['nombre', 'nit', 'email']
    list_filter = ['fecha_registro']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo', 'productor', 'precio', 'unidad', 'activo', 'fecha_publicacion']
    search_fields = ['nombre', 'nombre_finca', 'ubicacion']
    list_filter = ['tipo', 'activo', 'fecha_publicacion']
    readonly_fields = ['fecha_publicacion']


@admin.register(Normativa)
class NormativaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo_producto', 'fecha_actualizacion']
    search_fields = ['titulo', 'descripcion']
    list_filter = ['tipo_producto', 'fecha_actualizacion']


@admin.register(PrecioMercado)
class PrecioMercadoAdmin(admin.ModelAdmin):
    list_display = ['tipo_producto', 'precio_promedio', 'unidad', 'fecha', 'fuente']
    search_fields = ['tipo_producto', 'fuente']
    list_filter = ['tipo_producto', 'fecha']


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_publicacion', 'activa']
    search_fields = ['titulo', 'resumen', 'contenido']
    list_filter = ['activa', 'fecha_publicacion']
    readonly_fields = ['fecha_publicacion']


@admin.register(TRM)
class TRMAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'valor']
    list_filter = ['fecha']
    ordering = ['-fecha']
