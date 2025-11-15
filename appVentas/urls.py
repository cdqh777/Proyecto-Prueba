from django.urls import path
from . import views

urlpatterns = [
    # Página inicial
    path("", views.pagina_inicial, name='pagina_inicial'),
    
    # Autenticación
    path("login/", views.login_view, name='login'),
    path("logout/", views.logout_view, name='logout'),
    
    # Clientes
    path("clientes/", views.lista_clientes, name='lista_clientes'),
    path("nuevo_cliente/", views.crear_cliente, name="crear_cliente"),
    path("eliminar_cliente/<int:id>/", views.eliminar_cliente, name="eliminar_cliente"),
    path("actualizar_cliente/<int:id>/", views.actualizar_cliente, name='actualizar_cliente'),
    
    # Tiendas
    path("tiendas/", views.lista_tiendas, name='lista_tiendas'),
    path("nueva_tienda/", views.crear_tienda, name="crear_tienda"),
    path("eliminar_tienda/<int:id>/", views.eliminar_tienda, name="eliminar_tienda"),
    path("actualizar_tienda/<int:id>/", views.actualizar_tienda, name='actualizar_tienda'),
    
    # Compras
    path("compras/", views.lista_compras, name='lista_compras'),
    path("nueva_compra/", views.crear_compra, name="crear_compra"),
    path("eliminar_compra/<int:id>/", views.eliminar_compra, name="eliminar_compra"),
    path("actualizar_compra/<int:id>/", views.actualizar_compra, name='actualizar_compra'),
]