from django.shortcuts import render, redirect
from home.models import Pessoa, Veiculo, Caminhoneiro, Caminhao
from django.contrib import messages

def index(request):
    people = {
        "pessoas": Pessoa.objects.select_related('veiculo').all()
    }
    return render(request, 'index.html', people)

def insert_data(request):
    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.Email = request.POST.get('email')
        pessoa.Nome = request.POST.get('nome')
        pessoa.save()
        return redirect('index')
    
def deletar_pessoa(request, id):
    if request.method == 'GET':
        pessoa = Pessoa.objects.get(Id=id)
        pessoa.delete()
        messages.success(request, message='Deletado com sucesso')
        return redirect('index')

def caminhoneiro_index(request):
    caminhoneiro = Caminhoneiro.objects.select_related('Caminhao').all()
    caminhoneiros = {
        "caminhoneiros": caminhoneiro,
    }
    return render(request, 'caminhoneiro.html', caminhoneiros)


def adiciona_caminhoneiro(request):
    try:
        if request.method == "POST":
            caminhoneiro = Caminhoneiro()
            caminhoneiro.Nome = request.POST.get('nome')
            caminhoneiro.Email = request.POST.get('email')
            caminhoneiro.Caminhao = Caminhao.objects.get(Id=1)
            caminhoneiro.save()
            return redirect('caminhoneiro_index')
    except:
        print("Aconteceu um erro")

def deletar_caminhoneiro(request, id):
    try:
        if request.method == 'GET':
            caminhoneiro = Caminhoneiro.objects.get(Id=id)
            caminhoneiro.delete()
            messages.success(request, message='Deletado com sucesso')
            return redirect('caminhoneiro_index')
    except:
        print("Aconteceu um erro")