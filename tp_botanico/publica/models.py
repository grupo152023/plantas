from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to="producto", null=True)
    stock  = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre}"

class Planta(Producto):
    SOL = 'Sol'
    SOMBRA = 'Sombra'
    INTERIOR = 'Interior'
    EXTERIOR = 'Exterior'
    
    AMBIENTE_CHOICES = (
        (SOL, 'Sol'),
        (SOMBRA, 'Sombra'),
        (INTERIOR, 'Interior'),
        (EXTERIOR, 'Exterior')
    )
    ambiente = models.CharField(
        max_length=10,
        choices=AMBIENTE_CHOICES,
        default=INTERIOR)
    


class GrupoPlanta(models.Model):
    codigo = models.CharField(max_length=128)
    descripcion = models.ManyToManyField(Planta, through="TipoPlanta")
   
    def __str__(self):
        return self.codigo

class TipoPlanta(models.Model):
    producto = models.ForeignKey(Planta, on_delete=models.CASCADE)
    grupos = models.ForeignKey(GrupoPlanta, on_delete=models.CASCADE)
    caracteristicas = models.CharField(max_length=164)

    def __str__(self):
        return self.caracteristicas


class Factura(models.Model):
    numero_factura = models.IntegerField(default=0)
    fecha = models.DateTimeField(default=timezone.now)
    cuit   = models.CharField(max_length=128)
    importe = models.FloatField()


    def __str__(self):
        return f"{self.numero_factura}"


class ProductoFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    linea = models.IntegerField(default=0)
    cantidad =  models.IntegerField(default=0)
    precio = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.factura,self.producto}"




class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(default="./perfil/plantita.png", upload_to="perfil", null=True)

    def __str__(self):
        return f"Perfil de {self.user}"
    
    def seguidores(self):
        user_ids = Relacion.objects.filter(desde_user=self.user)\
                            .values_list("a_user_id", flat=True)
        return User.objects.filter(id__in=user_ids)
    
    def seguidos(self):
        user_ids = Relacion.objects.filter(a_user=self.user)\
                            .values_list("desde_user_id", flat=True)
        return User.objects.filter(id__in=user_ids)
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
    fechaPost = models.DateTimeField(default=timezone.now)
    contenido = models.TextField()

    class Meta:
        ordering = ["-fechaPost"]
    
    def __str__(self):
        return f"{self.user.username}: {self.contenido}"

class Relacion(models.Model):
    desde_user = models.ForeignKey(User, related_name="relacion", on_delete=models.CASCADE)
    a_user = models.ForeignKey(User, related_name="a_relacion", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.desde_user} a {self.a_user}"

    