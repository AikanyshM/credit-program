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
        widgets = {'application_date': forms.widgets.DateInput(attrs={'type': 'date'})}



class ProgramForm(forms.Form):
    name = forms.CharField(max_length=100, label="Наименование программы")
    max_credit = forms.IntegerField(label="Максимальная сумма займа")
    interest_rate = forms.FloatField(label="Процентная ставка")
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

class ClientsForm(forms.Form):
    first_last_name = forms.CharField(max_length=200, label="ФИО клиента")
    INN = forms.CharField(max_length=10, label="ИНН")
    phone_number = forms.CharField(max_length=15, label="номер телефона")
    address = forms.CharField(max_length=20, label="адрес клиента")
    application_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    credit_program = forms.CharField(max_length=50)
    STATUS_TYPE = (
        ('Pending', 'На рассмотрении'), ('Received','Получил'),
        ('Paid out','Выплатил'), ('Denied','Отказано')
        )
    status = forms.CharField(max_length=50)

    

