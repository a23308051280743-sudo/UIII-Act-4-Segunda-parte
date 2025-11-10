from django.db import models

class Habitacion(models.Model):
    numero = models.PositiveIntegerField(unique=True)

    # ✅ Aquí acomodas los 3 campos con default
    capacidad = models.PositiveIntegerField(default=1)
    ubicacion = models.CharField(max_length=100, default='Sin asignar')
    tipo = models.CharField(max_length=50, choices=[
        ('Sencilla', 'Sencilla'),
        ('Doble', 'Doble'),
        ('Suite', 'Suite')
    ], default='Sencilla')

    precio = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    ocupada = models.BooleanField(default=False)

    def __str__(self):
        return f"Habitación {self.numero} - {self.tipo}"
