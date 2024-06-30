from django.shortcuts import render
from rest_framework import viewsets
from .models import MaleUser
from .serializers import MaleUserSerializer, MaleUserCreateSerializer, MaleUserUpdateSerializer

# ルート画面
def home_view(request):
    return render(request, 'home.html')

# Create your views here.
class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MaleUser.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return MaleUserCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return MaleUserUpdateSerializer
        return MaleUserSerializer
