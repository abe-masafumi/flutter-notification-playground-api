from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CustomUser, CustomUserSerializer

# ルート画面
def home_view(request):
    return render(request, 'home.html')
    
# カスタムビューを基点に処理
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CustomUserSerializer