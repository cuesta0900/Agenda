from django import forms
from django.core.exceptions import ValidationError
from contact import models


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
                
            }
        )
    )
    
    first_name = forms.CharField(#sobrescreve o first_name da Model
        widget=forms.TextInput(
            attrs={ #atributos do HTML
                'class': 'classe-html',
                'placeholder': 'Escreve aqui...'
            }
        ),
        label = 'Primeiro Nome',
        help_text='Texto de ajuda para o usuário'
    )
    
    class Meta:
        model = models.Contact
        fields = (#tuple
            'first_name', 'last_name', 'phone', 'email', 'description', 'category',
            'picture'
        )
        
    def clean(self): #tratativa dos erros do form
        cleaned_data = self.cleaned_data #leitura dos dados enviados
        #erros que serão exibidos, ainda sem validação
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        
        if first_name == last_name:
            msg = ValidationError('Primeio nome não pode ser igual ao último', code='invalid')
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
            
        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Não digite ABC',
                    code='invalid'
                ))
        return first_name