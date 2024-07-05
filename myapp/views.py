from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from .serializers import CustomUser, CustomUserCreateSerializer, MaleUser, MaleUserUpdateSerializer, MaleUserRetrieveSerializer, Hobby, HobbySerializer, FemaleUser, FemaleUserUpdateSerializer, FemaleUserRetrieveSerializer

# ルート画面
def home_view(request):
    return render(request, 'home.html')

# カスタムビューを基点に処理
class CustomUserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserCreateSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CustomUserCreateSerializer

# 男性ユーザー情報操作
class MaleUserViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = MaleUser.objects.all()

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return MaleUserUpdateSerializer
        elif self.action == 'retrieve':
            return MaleUserRetrieveSerializer
        
    # 削除処理でレスポンスデータを返す
    def destroy(self, request, *args, **kwargs):
            instance = self.get_object()
            instance.delete()
            return Response({'detail': 'Deletion was successful.'}, status=status.HTTP_204_NO_CONTENT)

# 趣味の作成、削除
class HobbyViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Hobby.objects.all()
    serializer_class = HobbySerializer

    def perform_create(self, serializer):
        user_id = self.request.data.get('user')
        user = MaleUser.objects.get(user=user_id)
        serializer.save(user=user)

    # 削除処理でレスポンスデータを返す
    def destroy(self, request, *args, **kwargs):
            instance = self.get_object()
            instance.delete()
            return Response({'detail': 'Deletion was successful.'}, status=status.HTTP_204_NO_CONTENT)

# 女性ユーザー情報操作
class FemaleUserViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = FemaleUser.objects.all()

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return FemaleUserUpdateSerializer
        elif self.action == 'retrieve':
            return FemaleUserRetrieveSerializer
        
    # 削除処理でレスポンスデータを返す
    def destroy(self, request, *args, **kwargs):
            instance = self.get_object()
            instance.delete()
            return Response({'detail': 'Deletion was successful.'}, status=status.HTTP_204_NO_CONTENT)