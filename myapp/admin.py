from django.contrib import admin
from .models import CustomUser, MaleUser, FemaleUser, ProfileImage, Hobby, ApiLog

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(MaleUser)
admin.site.register(FemaleUser)
admin.site.register(ProfileImage)
admin.site.register(Hobby)
admin.site.register(ApiLog)