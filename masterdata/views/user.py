from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from masterdata.forms.user import CadastroForms

def cadastro(request):

    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form.is_valid():
            if form['senha'].value() != form['senha_confirmacao'].value():
                messages.error(request, 'As senhas digitadas não conferem')
                return redirect('cadastro')
            nome=form['nome_cadastro'].value()
            email=form['email'].value()
            senha=form['senha'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existente')
                return redirect('cadastro')
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, f'Usuário {nome} cadastrado com sucesso!')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não autenticado!')
        return redirect('login')
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')