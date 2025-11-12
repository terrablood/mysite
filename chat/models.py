from django.db import models
from django.contrib.auth.models import User

class Jatek(models.Model):
    aknaszám = models.IntegerField()
    egyik = models.ForeignKey(User, on_delete=models.PROTECT)
    masik = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name='masik')
    nyertes = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name='nyertes')
    nev = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Játék'
        verbose_name_plural = 'Játékok'

    def __str__(self):
        return f' {self.nev}: {self.egyik} vs {self.masik}'
    


# ha létre lett hozva, migrálni kell
# aknaszám egyik masik nyertes nev