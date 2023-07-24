from django.db import models

class Cliente(models.Model):
    dni = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    email = models.EmailField(max_length=100)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.dni)

class Actividad(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.PositiveSmallIntegerField(primary_key=True)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.codigo)

class Pago(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    monto = models.PositiveSmallIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    dni_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)   

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.dni_cliente, self.fecha)


class Inscripcion(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    dni_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.dni_cliente, self.actividad)