from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response

from account.serializers import RegisterSerializer

User = get_user_model()


class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response("Успешно зарегестрированны", status=201)
