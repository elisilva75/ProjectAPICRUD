# codeleap_backend/careers/urls.py

from django.urls import path
from .views import CareerPostListCreateView, CareerPostUpdateDeleteView

urlpatterns = [
    # URL para listar e criar posts
    path('', CareerPostListCreateView.as_view(), name='post-list-create'),

    # URL para atualizar e deletar posts
    path('<int:pk>/', CareerPostUpdateDeleteView.as_view(), name='post-update-delete'),

    # Adicionando rota para atualizar (PATCH) um post específico
    path('<int:pk>/update/', CareerPostUpdateDeleteView.as_view(), name='post-update'),

    # Adicionando rota para deletar (DELETE) um post específico
    path('<int:pk>/delete/', CareerPostUpdateDeleteView.as_view(), name='post-delete'),
]
