from django.db import models
import datetime as dt
import statistics as stats

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=60)
    num_id = models.CharField(max_length=11)
    fec_nac = models.DateField()

    def edad(self):
        hoy = dt.date.today()
        edad = hoy - self.fec_nac
        return int(edad.days/365)
    def __str__(self):
        edad = self.edad()
        return "%s %s -- ID: %s -- Edad: %s Años" %(self.nombre, self.apellidos, self.num_id, edad)

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=60)
    num_id = models.CharField(max_length=11)

    def __str__(self):
        return 'Profesor: %s %s' %(self.nombre, self.apellidos)

class Curso(models.Model):
    grado_CHOICES = [
        ('0', 'Transición'),
        ('1', 'Primero'),
        ('2', 'Segundo'),
        ('3', 'Tercero'),
        ('4', 'Cuarto'),
        ('5', 'Quinto'),
        ('6', 'Sexto'),
        ('7', 'Séptimo'),
        ('8', 'Octavo'),
        ('9', 'Noveno'),
        ('10', 'Décimo'),
        ('11', 'Undécimo')
    ]
    grado = models.CharField(max_length=2, choices=grado_CHOICES, default='0')

    def __str__(self):
        grado_str = 'N/A'
        for i in self.grado_CHOICES:
            if(self.grado == i[0]):
                grado_str = i[1]
        return grado_str

class Grupo(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=2)
    dir_grupo = models.OneToOneField(Profesor, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' %(self.curso, self.nombre)   
    
class Matricula(models.Model):
    estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return "%s Matriculado en el Curso: %s" %(self.estudiante, self.curso)

class Asignatura(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return '%s -- Profesor: %s' %(self.nombre, self.profesor)

class Horario(models.Model):
    dias = (
        ('L', 'Lunes'),
        ('M', 'Martes'),
        ('Mi', 'Miercoles'),
        ('J', 'Jueves'),
        ('V', 'Viernes')
    )
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    dia = models.CharField(max_length=2, choices=dias, default='L')
    hora = models.TimeField()

    def __str__(self):
        return "Asignatura: %s -- %s %s" %(self.asignatura, self.dia, self.hora)  

class Calificacion(models.Model):
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    nota_1 = models.IntegerField()
    nota_2 = models.IntegerField()
    nota_3 = models.IntegerField()
    nota_4 = models.IntegerField()

    def nota_final(self):
        nota = (self.nota_1 + self.nota_2 + self.nota_3 + self.nota_4) / 4
        return nota  
  

    
    
