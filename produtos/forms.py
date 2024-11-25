from django import forms 
from produtos.models import Categoria, Produto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        labels = {
            'nome': 'nome da Categoria'

        }

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','preco','categoria','imagem']
        labels= {
                    'nome':'nome do Produto',
                    'preco':'preco (R$)',
                    'categoria':'Categoria',
                    'imagem':'Imagemdo Produto',
                }