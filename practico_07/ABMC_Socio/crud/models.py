from django.db import models


class Socio(models.Model):
    id_socio = models.AutoField(primary_key=True)
    dni = models.TextField(max_length=8)
    name = models.TextField(max_length=30)
    surname = models.TextField(max_length=30)


