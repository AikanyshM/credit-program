from django.db import models

class CreditProgram(models.Model):
    name = models.CharField(max_length=100)
    max_credit = models.IntegerField()
    interest_rate = models.FloatField()
    commission_amount = models.CharField(max_length=4)

    def __str__(self):
        return self.name

    
class Client(models.Model):
    first_last_name = models.CharField(max_length=200)
    INN = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=20)
    application_date = models.DateField()
    credit_program = models.ForeignKey(CreditProgram, default="ипотечный", on_delete=models.CASCADE)
    STATUS_TYPE = (
        ('Pending', 'На рассмотрении'), ('Received','Получил'),
        ('Paid out','Выплатил'), ('Denied','Отказано')
        )
    status = models.CharField(max_length=50, default="На рассмотрении", choices=STATUS_TYPE)

    def __str__(self):
        return self.first_last_name
