from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    class Meta:
        managed = False
        db_table = 'clientes'
    
    # ⭐ AGREGAR ESTO
    def __str__(self):
        return f"{self.id_cliente} - {self.nombre}"

class Tienda(models.Model):
    id_tienda = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'tiendas'
    
    # ⭐ AGREGAR ESTO
    def __str__(self):
        return f"{self.id_tienda} - {self.nombre}"

class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    
    cliente = models.ForeignKey(
        Cliente,
        on_delete= models.CASCADE,
        db_column='id_cliente',
        related_name='compras'
    )

    tienda = models.ForeignKey(
        Tienda,
        on_delete= models.CASCADE,
        db_column='id_tienda',
    )
    
    class Meta:
        managed = False
        db_table = 'compras'
    
    # ⭐ OPCIONAL
    def __str__(self):
        return f"Compra #{self.id_compra} - {self.monto}"