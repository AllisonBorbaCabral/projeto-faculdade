from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Usuário',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nome de usuário',
            }
        )
    )
    password = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Senha',
            }
        ),
    )


class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Usuário',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'João Silva'
            }
        )
    )
    email=forms.EmailField(
        label='E-mail',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'joaosilva@xpto.com'
            }
        )
    )
    senha=forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        ),
    )
    senha_confirmacao=forms.CharField(
        label='Confirme a senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirme sua senha'
            }
        ),
    )

    def clean_nome_cadastro(self):
        '''Precisa iniciar com clean seguido do nome do campo que quero validar'''
        nome=self.cleaned_data.get('nome_cadastro')
        if nome:
            nome=nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Não é possível inserir espaços em branco dentro do campo usuário')
            else:
                return nome
    
    def clean_senha_confirmacao(self):
        senha = self.cleaned_data.get('senha')
        senha_confirmacao = self.cleaned_data.get('senha_confirmacao')
        if senha != senha_confirmacao:
            raise forms.ValidationError('As senhas digitadas não conferem')
        else:
            return senha_confirmacao
        
                