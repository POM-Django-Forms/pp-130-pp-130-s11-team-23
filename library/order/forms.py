from django import forms
from .models import Order
from book.models import Book
from django.utils.timezone import make_aware
from datetime import datetime
from django.utils.timezone import now

class OrderForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.all(), label='Книга')
    plated_end_at = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Запланована дата повернення'
    )

    def clean_plated_end_at(self):
        date = self.cleaned_data['plated_end_at']
        if date < datetime.today().date():
            raise forms.ValidationError("Дата не може бути в минулому.")
        return make_aware(datetime.combine(date, datetime.min.time()))
    
    
class CloseOrderForm(forms.Form):
    end_at = forms.DateField(
        initial=now,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Фактична дата повернення"
    )