import django_filters
from django import forms
from .models import GameResult

myDateInput = forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'})


class GameResultFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(field_name='last_name', lookup_expr='icontains')
    date = django_filters.DateFilter(field_name='date_time_created__date', lookup_expr='exact', widget=myDateInput)

    class Meta:
        model = GameResult
        fields = []