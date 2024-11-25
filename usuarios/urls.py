from django.urls import path
from .views import EditPerfilView, LoginView, LogoutView, PerfilView

urlpatterns = [
    path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('editarperfil/', EditPerfilView.as_view(), name='edit_perfil'),
    path('perfil/', PerfilView.as_view(), name='perfil'),
]
