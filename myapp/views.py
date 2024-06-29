from django.shortcuts import render
from rest_framework import viewsets
from .models import MaleUser
from .serializers import MaleUserSerializer

# ルート画面
def home_view(request):
    return render(request, 'home.html')

# Create your views here.
class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MaleUser.objects.all()
    serializer_class = MaleUserSerializer
