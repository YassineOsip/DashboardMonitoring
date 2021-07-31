from django.contrib import admin
from DashboardMonitoring import models

admin.site.register(models.Chain)
admin.site.register(models.Product)
admin.site.register(models.ProductivityPerHour)

