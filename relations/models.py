# Create your models here.
from django.db import models


class Creator(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Meta:
    ordering = ['first_name']

# * one2one relation:


class Language(models.Model):
    name = models.CharField(max_length=50)
    creator = models.OneToOneField(Creator, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.creator}"

    class Meta:
        ordering = ['name']


#! CASCADE  - parent silinince silinir
#! SET_NULL  - parent silinince null yapar
#! PROTECT   - parent silinince hata verir
#! DO_NOTHING - parent silinince hiçbir şey yapmaz
#! SET_DEFAULT - parent silinince default değer atar


# * many2one relation:

class Framework(models.Model):
    name = models.CharField(max_length=50)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.language}"

    class Meta:
        ordering = ['name']


# * many2many relation:
class Developer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # Dont use on_delete=models.CASCADE
    framework = models.ManyToManyField(Framework)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

    class Meta:
        ordering = ['first_name']
