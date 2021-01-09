from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from apps.products.models.products import Products
from apps.products.serializers.products_serializer import (
    ProductsSerializer,
    ProductsPatchSerializer
)


class ProductsView(viewsets.GenericViewSet):

    queryset = Products.objects.filter(is_active=True).order_by('-quantity')

    def get_serializer_class(self):
        if self.action == "partial_update":
            return ProductsPatchSerializer
        return ProductsSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.get_serializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        query = get_object_or_404(self.get_queryset(), code=pk)
        serializer = self.get_serializer(query, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        model = get_object_or_404(self.get_queryset(), code=pk)
        serializer = self.get_serializer(model, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        model = get_object_or_404(self.get_queryset(), code=pk)
        serializer = self.get_serializer(model, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)