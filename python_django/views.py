from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProgramForm, CreditForm, ClientForm
from .models import CreditProgram, Client
from django.urls import reverse

def test_form(request):
    return render(request, 'test_form.html')


def program_form(request):
    if request.method == "GET":
        form = ProgramForm()
        return render(request, 'program_form.html', {'form': form})
    if request.method == "POST":
        form = ProgramForm(request.POST)
        if form.is_valid():
            return HttpResponse("Все сохранено!")
        else:
            return render(request, 'program_form.html', {'form': form})


def credit_form(request):
    if request.method == "GET":
        form = CreditForm()
        return render(request, 'program_form.html', {'form': form})
    if request.method == "POST":
        form = CreditForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('all_credits'))
        else:
            return render(request, 'program_form.html', {'form': form})


def client_form(request):
    if request.method == "GET":
        credit_program = CreditProgram.objects.all()
        form = ClientForm()
        return render(request, 'program_form.html', {'form': form, "credit_program": credit_program})
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Data saved")
        else:
            return render(request, 'program_form.html', {'form': form})

def search(request):
    client_name = request.GET.get('first_last_name')
    return HttpResponse(client_name)

def client_view(request):
    clients = Client.objects.all()
    return render(request, 'clients_list.html', {'clients': clients})

def credit_view(request):
    credits = CreditProgram.objects.all()
    return render(request, 'credits_list.html', {'credits': credits})