from django.urls import path
from .views import CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView, ProdutoCreateView, ProdutoDeleteView, ProdutoListView

urlpatterns = [
    path('categorias/', CategoriaListView.as_view(), name = "categoria_list"),
    path('categorias/nova/', CategoriaCreateView.as_view(),name = 'categoria_create'),
    path('categoriaa/<int:pk>/editar/', CategoriaUpdateView.as_view(),name= 'categoria_update'),
    path('categorias/<int:pk>/excluir/', CategoriaDeleteView.as_view(), name= 'categoria_delete'),

    path('produtos/',ProdutoListView.as_view(), name = 'produto_list'),
    path('produtos/novo/',ProdutoCreateView.as_view(), name = 'produto_create'),
    path('produtos/<int:pk>/excluir/', ProdutoCreateView.as_view(), name= 'produto_update'),
    path('produtos/<int:pk>/excluir/', ProdutoDeleteView.as_view(), name= 'produto_delete'),
]

