from homepage.views import ProdutoSaldoView
from django.urls import path

urlpatterns = [
    path('',ProdutoSaldoView.as_view(), name="homepage"),

]
