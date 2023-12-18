from django.core.mail import send_mail
from rest_framework import generics
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from .utils import send_email


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        #send_email.delay(instance.id)  # Call the Celery task to send email
        
        return Response(serializer.data)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        return Response(serializer.data)


