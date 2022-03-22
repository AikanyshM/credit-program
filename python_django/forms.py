from django import forms
from django.core.exceptions import ValidationError
from .models import CreditProgram, Client

class CreditForm(forms.ModelForm):
    class Meta:
        model = CreditProgram
        fields = "__all__"

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"



class ProgramForm(forms.Form):
    name = forms.CharField(max_length=100, label="Наименование программы")
    max_credit = forms.IntegerField(label="Максимальная сумма займа")
    interest_rate = forms.DecimalField(max_digits=4, decimal_places=2, label="Процентная ставка")
    commission_amount = forms.CharField(max_length=4, label="сумма комиссии")

    def clean_max_credit(self):
        data = self.cleaned_data['max_credit']
        if data < 0:
            raise ValidationError("Максимальный кредит не может быть отрицательным")
        return data
    
    def clean_interest_rate(self):
        data = self.cleaned_data['interest_rate']
        if data < 0:
            raise ValidationError("Процентная ставка не может быть отрицательной")
        return data

    

