from django.db import models

class Chain(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, null=False, blank=False)
    obj = models.PositiveIntegerField(null=False, blank=False)


class Product(models.Model):
    def __str__(self):
        return self.name + '/' + self.ref

    chain = models.ManyToManyField(Chain, blank=False)
    ref = models.CharField(max_length=100, primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    quantity = models.PositiveIntegerField(null=False, blank=False, default=0)


class ProductivityPerHour(models.Model):
    def __str__(self):
        return self.chain.name + '-' + str(self.hour) + 'H'

    chain = models.ForeignKey(Chain, on_delete=models.CASCADE, null=False, blank=False)
    products = models.ManyToManyField(Product, blank=True)
    hour = models.PositiveIntegerField(blank=False, null=False)
    productivity = models.PositiveIntegerField(null=False, blank=False)
    retouch = models.PositiveIntegerField(null=False, blank=False, default=0)
    latest_modification = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("chain", "hour"),)
