from django.shortcuts import render
from rest_framework import viewsets, exceptions
from .serializers import CustomUser, CustomUserCreateSerializer, MaleUserUpdateSerializer, MaleUser, MaleUserRetrieveSerializer

# ルート画面
def home_view(request):
    return render(request, 'home.html')

# カスタムビューを基点に処理
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CustomUserCreateSerializer
        else:
            raise exceptions.MethodNotAllowed(self.action)
        
class MaleUserViewSet(viewsets.ModelViewSet):
    queryset = MaleUser.objects.all()

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return MaleUserUpdateSerializer
        elif self.action == 'retrieve':
            return MaleUserRetrieveSerializer
        else:
            raise exceptions.MethodNotAllowed(self.action)
