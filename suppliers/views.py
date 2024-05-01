from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from users.models import User
from suppliers.models import Supplier
from products.permissions import IsAdmin, IsOwner
from suppliers.serializers import SupplierSerializer
from suppliers.filters import SupplierFilter
from django_filters.rest_framework import DjangoFilterBackend


class SupplierViewSet(viewsets.ModelViewSet):
    """Supplier ViewSet"""

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SupplierFilter

    def get_permissions(self):
        """Распределение прав доступа"""

        if self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsOwner | IsAdmin]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """
        Создание продукта и хозяина продукта.
        """
        supplier = serializer.save()
        supplier.user = get_object_or_404(User, id=self.request.user.id)
        supplier.save()
