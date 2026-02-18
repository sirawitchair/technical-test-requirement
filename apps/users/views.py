from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from .models import User, UserProfile
from .serializers import UserSerializer, UserProfileSerializer


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'page': self.page.number,
            'page_size': self.get_page_size(self.request),
            'total_pages': self.page.paginator.num_pages,
            'total_items': self.page.paginator.count,
            'results': data
        })


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = User.objects.all()
        search = self.request.query_params.get('search')
        sortby = self.request.query_params.get('sortby', 'created_at')
        sorttype = self.request.query_params.get('sorttype', 'desc')

        if search:
            queryset = queryset.filter(
                Q(username__icontains=search) | Q(email__icontains=search)
            )

        if sorttype.lower() == 'desc':
            sortby = f'-{sortby}'
        queryset = queryset.order_by(sortby)

        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(True, status=status.HTTP_201_CREATED)


class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = UserProfile.objects.all()
        search = self.request.query_params.get('search')
        sortby = self.request.query_params.get('sortby', 'created_at')
        sorttype = self.request.query_params.get('sorttype', 'desc')

        if search:
            queryset = queryset.filter(
                Q(first_name_th__icontains=search) |
                Q(last_name_th__icontains=search) |
                Q(first_name_en__icontains=search) |
                Q(last_name_en__icontains=search)
            )

        if sorttype.lower() == 'desc':
            sortby = f'-{sortby}'
        queryset = queryset.order_by(sortby)

        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(True, status=status.HTTP_201_CREATED)
