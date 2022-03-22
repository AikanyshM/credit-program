from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProgramForm, CreditForm, ClientForm, ClientsForm
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

def clients_form(request):
    if request.method == "GET":
        credit_program = CreditProgram.objects.all()
        form = ClientsForm()
        return render(request, 'clients_form.html', {'form': form, "credit_program": credit_program})
    if request.method == "POST":
        form = ClientsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('all_clients'))
        else:
            return render(request, 'clients_form.html', {'form': form, "credit_program": credit_program})



def credit_form(request):
    if request.method == "GET":
        credit_program = CreditProgram.objects.all()
        form = CreditForm()
        return render(request, 'program_form.html', {'form': form, "credit_program": credit_program})
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
            return redirect(reverse('all_clients'))
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

def filter_clients(request, id):
    clients = Client.objects.filter(credit__id = id)
    return render(request, 'clients_list.html', {'clients': clients})

def detail_view(request, id):
    single_client = Client.objects.get(id=id)
    return render(request, 'single_client.html', {'single_client': single_client})

def delete_client(request, id):
    delete_client = Client.objects.get(id=id)
    delete_client.delete()
    return redirect(reverse('all_clients'))

def delete_credit(request, id):
    delete_credit = CreditProgram.objects.get(id=id)
    delete_credit.delete()
    return redirect(reverse('all_credits'))

def update_client(request, id):
    single_client = Client.objects.get(id=id)
    if request.method == "GET":
        credit_program = CreditProgram.objects.all()
        context = {
            'credit_program': credit_program,
            'single_client': single_client
        }
        return render(request, 'update_client.html', context) 
    
    if request.method == "POST":
        form = ClientsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('all_clients'))
        else:
            return render(request, 'clients_form.html', {'form': form, "credit_program": credit_program})


