from django.db import models

# Create your models here.

class Vater(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50, primary_key=True)
    gehalt = models.DecimalField(verbose_name="Einkommen", max_digits=8, decimal_places=2)
    
    class Meta:
        verbose_name = "Vater"
        verbose_name_plural = "Väter"

    def __str__(self):
        return self.name


class Mutter(models.Model):
    name = models.CharField(verbose_name="Mutter", max_length=50)
    gatte = models.ForeignKey(Vater, verbose_name="Ehegatte", on_delete=models.PROTECT)
    kochkunst = models.DecimalField("Lecker Essen", max_digits=2, decimal_places=1)
    
    class Meta:
        verbose_name = "Mutter"
        verbose_name_plural = "Mütter"

    def __str__(self):
        return f"Name: {self.name} -- Gatte: {self.gatte.name}."
    
class Kind(models.Model):
    name = models.CharField(verbose_name="Kind", max_length=50, primary_key=True) 
    mutter = models.ForeignKey(Mutter, verbose_name="Mutter", on_delete=models.PROTECT)
    noten = models.DecimalField("Schulnoten", max_digits=5, decimal_places=2)
    class Meta:
        verbose_name = "Kind"
        verbose_name_plural = "Kinder"

    def __str__(self):
        return f"Kind: {self.name}, Mutter: {self.mutter.name}, Vater: {self.mutter.gatte.name}"
