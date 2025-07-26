from django.contrib import admin
from .models import StockData, ForecastResult


@admin.register(StockData)
class StockDataAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'date', 'close_price', 'volume')
    list_filter = ('symbol', 'date')
    search_fields = ('symbol',)
    ordering = ('-date',)


@admin.register(ForecastResult)
class ForecastResultAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'forecast_date', 'predicted_price', 'model_used')
    list_filter = ('symbol', 'model_used', 'forecast_date')
    search_fields = ('symbol',)
    ordering = ('-created_at',)
