from django.db import models


class BodyPart(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MuscleGroup(models.Model):
    name = models.CharField(max_length=100)
    ar_name = models.CharField(max_length=255, null=True)
    body_part = models.ForeignKey(BodyPart, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Muscle(models.Model):
    name = models.CharField(max_length=100)
    ar_name = models.CharField(max_length=255)
    muscle_group = models.ForeignKey(MuscleGroup, on_delete=models.SET_NULL, null=True)
