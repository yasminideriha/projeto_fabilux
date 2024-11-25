from django.urls import path
from .views import MovimentacaoList,MovimentacaoDeleteView, MovimentacaoCreateView, MovimentacaoUpdateView


urlpatterns = [
    path('movimentacao/', MovimentacaoList.as_view(),name='movimentacao_list'),
    path('movimentacao/nova/', MovimentacaoCreateView.as_view(),name='movimentacao_create'),
    path('movimentacao/<int:pk>/editar/', MovimentacaoUpdateView.as_view(),name= 'movimentacao_update'),
    path('movimentacao/<int:pk>/excluir/', MovimentacaoDeleteView.as_view(), name='movimentacao_delete'),


]
