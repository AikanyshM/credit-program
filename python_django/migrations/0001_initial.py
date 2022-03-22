# Generated by Django 3.2 on 2022-03-22 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreditProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('max_credit', models.IntegerField()),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('commission_amount', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_last_name', models.CharField(max_length=200)),
                ('INN', models.CharField(max_length=10)),
                ('Phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=20)),
                ('application_date', models.DateField()),
                ('status', models.CharField(choices=[('Pending', 'На рассмотрении'), ('Received', 'Получил'), ('Paid out', 'Выплатил'), ('Denied', 'Отказано')], default='На рассмотрении', max_length=50)),
                ('credit_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='python_django.creditprogram')),
            ],
        ),
    ]
