from django.db import models


class Breeds(models.Model):
    name = models.CharField(max_length=100, verbose_name="Pavadinimas")
    country = models.CharField(max_length=100, verbose_name="Šalis")
    height = models.CharField(max_length=20, verbose_name="Maksimalus ūgis")
    lifespan = models.CharField(max_length=5, verbose_name="Gyvenimo trukmė")
    description = models.TextField(blank=True, verbose_name="Aprašymas")
    photo = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Veislė'
        verbose_name_plural = 'Veislės'
        ordering = ['name', 'country']
