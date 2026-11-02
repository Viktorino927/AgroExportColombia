from django.contrib import admin
from django.urls import path
from agro_export import views


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Página principal
    path('', views.home, name='home'),
    
    # Normatividad
    path('normatividad/', views.normatividad, name='normatividad'),
    
    # Productos
    path('productos/', views.productos, name='productos'),
    
    # Usuarios
    path('usuarios/', views.usuarios_view, name='usuarios'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
  
    
    # Perfil de productor
    path('perfil/', views.perfil_productor, name='perfil_productor'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('editar-producto/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('eliminar-producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]

