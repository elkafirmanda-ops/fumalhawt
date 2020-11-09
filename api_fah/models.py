from django.db import models

class Alquran(models.Model):
    id = models.AutoField(primary_key=True)
    surat = models.IntegerField(blank=False, null=False, default=0)
    ayat = models.IntegerField(blank=False, null=False, default=0)
    arab = models.TextField()
    indonesia = models.TextField()
    def __str__(self):
        return self.arab, self.indonesia