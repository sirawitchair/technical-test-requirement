from rest_framework.viewsets import ModelViewSet
from .models import User, UserProfile
from .serializers import UserSerializer, UserProfileSerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = User.objects.all()
        if self.request.query_params.get('search'):
            queryset = queryset.filter(Q(username__icontains=self.request.query_params.get('search')) | Q(email__icontains=self.request.query_params.get('search')))
        if self.request.query_params.get('ordering'):
            queryset = queryset.order_by(self.request.query_params.get('ordering'))
        return queryset
    
    def retrieve(self, request):
        response = {
            'status': 'success',
            'data': self.get_queryset().filter(id=request.user.id)
        }
        return response

    def list(self, request):
        response = {
            'status': 'success',
            'data': self.get_queryset()
        }
        return response

class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = UserProfile.objects.all()
        if self.request.query_params.get('search'):
            queryset = queryset.filter(Q(first_name_th__icontains=self.request.query_params.get('search')) | Q(last_name_th__icontains=self.request.query_params.get('search')) | Q(first_name_en__icontains=self.request.query_params.get('search')) | Q(last_name_en__icontains=self.request.query_params.get('search')))
        if self.request.query_params.get('ordering'):
            queryset = queryset.order_by(self.request.query_params.get('ordering'))
        return queryset
