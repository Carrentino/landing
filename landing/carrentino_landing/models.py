from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата подачи")

    def __str__(self):
        return f"{self.name} - {self.email}"
