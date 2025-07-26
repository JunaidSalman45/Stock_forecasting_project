from django import forms


class ForecastForm(forms.Form):
    STOCK_CHOICES = [
        ('AAPL', 'Apple Inc. (AAPL)'),
        ('GOOGL', 'Alphabet Inc. (GOOGL)'),
        ('MSFT', 'Microsoft Corporation (MSFT)'),
        ('TSLA', 'Tesla Inc. (TSLA)'),
        ('AMZN', 'Amazon.com Inc. (AMZN)'),
    ]
    
    MODEL_CHOICES = [
        ('arima', 'ARIMA Model'),
        ('linear', 'Linear Regression'),
        ('moving_average', 'Moving Average'),
    ]

    stock_symbol = forms.ChoiceField(
        choices=STOCK_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    forecast_days = forms.IntegerField(
        min_value=1,
        max_value=30,
        initial=7,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    
    model_type = forms.ChoiceField(
        choices=MODEL_CHOICES,
        initial='arima',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
