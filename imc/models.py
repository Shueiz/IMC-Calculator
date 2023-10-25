from django.db import models

class IMCResult(models.Model):
    height = models.FloatField()
    weight = models.FloatField()
    result = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'IMC Result {self.id}'