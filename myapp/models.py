import uuid
from django.db import models

class CustomUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ROLES = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    )
    firebase_uid = models.CharField(max_length=255, unique=True)
    role = models.CharField(max_length=10, choices=ROLES)
    username = models.CharField(max_length=100)
    birthday = models.DateField()

class MaleUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=255)
    introduction = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class FemaleUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    introduction = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class ProfileImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image_url = models.URLField()

    def __str__(self):
        return self.image_url

class Hobby(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(MaleUser, on_delete=models.CASCADE, related_name='hobbies')
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

class ApiLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    endpoint = models.CharField(max_length=255)
    request_time = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=10)
    status_code = models.IntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.endpoint} - {self.method}"