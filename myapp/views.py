from django.shortcuts import render
from rest_framework import viewsets, exceptions, status
from rest_framework.response import Response
from rest_framework import viewsets, exceptions
from .models import MaleUser
from .serializers import MaleUserCreateSerializer, MaleUserUpdateSerializer, MaleUserRetrieveSerializer

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
        elif self.action == 'retrieve':
            return MaleUserRetrieveSerializer
        else:
            raise exceptions.MethodNotAllowed(self.action)

# 削除処理でレスポンスデータを返す
    def destroy(self, request, *args, **kwargs):
            instance = self.get_object()
            instance.delete()
            return Response({'detail': 'Deletion was successful.'}, status=status.HTTP_204_NO_CONTENT)