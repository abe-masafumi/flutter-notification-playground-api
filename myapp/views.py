from django.shortcuts import render
from rest_framework import viewsets, exceptions, mixins
from .serializers import CustomUser, CustomUserCreateSerializer, MaleUserUpdateSerializer, MaleUser, MaleUserRetrieveSerializer, Hobby, HobbySerializer
from rest_framework.exceptions import ValidationError

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

class HobbyViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Hobby.objects.all()
    serializer_class = HobbySerializer

    # def get_queryset(self):
    #     return Hobby.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        user_id = self.request.data.get('user')
        try:
            user = MaleUser.objects.get(user=user_id)
        except MaleUser.DoesNotExist:
            raise ValidationError("User with the given ID does not exist")
        serializer.save(user=user)