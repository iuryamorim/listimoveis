from django import forms
from listimoveis.imoveis.models import Imovel


class ImoveisForm(forms.ModelForm):
    photo = forms.ImageField(label='Foto')

    class Meta:
        model = Imovel
        fields = ['name', 'address', 'photo', 'description', 'cep', 'slug']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control jqName'}),
            'address': forms.TextInput(attrs={'class': 'form-control jqAddress'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Somente números', 'maxlength': '8'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'rows': '3'}),
            'slug': forms.TextInput(attrs={'class': 'form-control jqSlug'}),
        }