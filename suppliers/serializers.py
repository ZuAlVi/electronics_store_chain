from rest_framework import serializers
from suppliers.models import Supplier
from products.serializers import ProductSerializer


class SupplierSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели Supplier
    """

    user_first_name = serializers.CharField(source="user.first_name", read_only=True)
    user_last_name = serializers.CharField(source="user.last_name", read_only=True)
    product = ProductSerializer(many=True, required=False)
    supplier = serializers.SlugRelatedField(slug_field='title', queryset=Supplier.objects.all())

    class Meta:
        model = Supplier
        fields = '__all__'
