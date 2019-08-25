from django.db import models

# Create your models here.

# Modelos DB

class Alumno(models.Model):
    apellidoPaterno = models.CharField(max_length= 35)
    apellidoMaterno = models.CharField(max_length= 35)
    nombres = models.CharField(max_length= 35)
    dni = models.CharField(max_length= 35)
    fechaNacimiento = models.DateField()
    SEXOS = (('F','Femenino'),('M','Masculino'))
    sexo = models.CharField(max_length=1, choices=SEXOS, default='M')

    def nombreCompleto(self):
        cadena = ' {0} {1} , {2}'
        return cadena.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

    def __str__(self):
        return self.nombreCompleto()

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return '{0} ({1})'.format(self.nombre, self.creditos)


class Matricula(models.Model):
    alumno = models.ForeignKey(Alumno, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fecha_matricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0} => {1}'.format(self.alumno , self.curso)
