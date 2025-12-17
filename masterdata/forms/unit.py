from django import forms

class UnitAddForm(forms.Form):
    name=forms.CharField(
        label='Nome',
        required=True,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Quilograma'
            }
        )
    )
    symbol=forms.CharField(
        label='Unidade',
        required=True,
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Kg'
            }
        )
    )
    is_active=forms.BooleanField(
        label='Ativo',
        # default=True,
         widget=forms.CheckboxInput(
             attrs={
                 'class': 'form-check-input',
             }
         ),
    )

    # def clean_nome_cadastro(self):
    #     '''Precisa iniciar com clean seguido do nome do campo que quero validar'''
    #     nome=self.cleaned_data.get('nome_cadastro')
    #     if nome:
    #         nome=nome.strip()
    #         if ' ' in nome:
    #             raise forms.ValidationError('Não é possível inserir espaços em branco dentro do campo usuário')
    #         else:
    #             return nome
    
    # def clean_senha_confirmacao(self):
    #     senha = self.cleaned_data.get('senha')
    #     senha_confirmacao = self.cleaned_data.get('senha_confirmacao')
    #     if senha != senha_confirmacao:
    #         raise forms.ValidationError('As senhas digitadas não conferem')
    #     else:
    #         return senha_confirmacao