# ui/views.py
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from masterdata.forms.user import LoginForm
from django.contrib.auth.views import LoginView

class UILoginView(LoginView):
    template_name = 'login/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        '''
        Chamado quando usuário e senha estão corretos
        '''
        response = super().form_valid(form)

        user = self.request.user
        messages.success(
            self.request,
            f'{user.first_name} {user.last_name} autenticado com sucesso!'
        )

        return response

    def form_invalid(self, form):
        '''
        Chamado quando usuário ou senha são inválidos
        '''
        messages.error(
            self.request,
            'Credenciais do usuário inválidas!'
        )
        return super().form_invalid(form)

    def get_success_url(self):
        '''
        Para garantir que SEMPRE vá para o index
        '''
        return reverse_lazy('ui:index')
