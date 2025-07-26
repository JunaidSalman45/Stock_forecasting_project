from django.db import models
from django.utils import timezone


class StockData(models.Model):
    symbol = models.CharField(max_length=10)
    date = models.DateField()
    open_price = models.DecimalField(max_digits=10, decimal_places=2)
    high_price = models.DecimalField(max_digits=10, decimal_places=2)
    low_price = models.DecimalField(max_digits=10, decimal_places=2)
    close_price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.BigIntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('symbol', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.symbol} - {self.date}"


class ForecastResult(models.Model):
    symbol = models.CharField(max_length=10)
    forecast_date = models.DateField()
    predicted_price = models.DecimalField(max_digits=10, decimal_places=2)
    confidence_lower = models.DecimalField(max_digits=10, decimal_places=2)
    confidence_upper = models.DecimalField(max_digits=10, decimal_places=2)
    model_used = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['forecast_date']

    def __str__(self):
        return f"{self.symbol} forecast for {self.forecast_date}"
