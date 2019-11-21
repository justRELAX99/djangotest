from django.db import models

class city(models.Model):
    name=models.CharField(max_length=30,verbose_name='Город')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural="Города"
        verbose_name="Город"
        ordering=["name"]