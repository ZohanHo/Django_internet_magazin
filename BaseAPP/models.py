from django.db import models

# Create your models here.

class Subscribers(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
        verbose_name = "Подпищик"
        verbose_name_plural = "Подпищики"

    def __str__(self):  #Выводит указаное поле в админке с названием указаным после селф, можно выводить пару полей
        return "{} {}".format(self.id, self.name)