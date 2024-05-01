from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from products.models import Product
from users.models import User
from products.permissions import IsAdmin, IsOwner
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """Product ViewSet"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

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
        product = serializer.save()
        product.user = get_object_or_404(User, id=self.request.user.id)
        product.save()
