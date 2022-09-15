from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from drf_yasg import openapi
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from datetime import datetime
from cicd.serializers import AddTokenSerilizer
from cicd.models import GithubToken


class AddTokenAPIView(GenericAPIView):

    @swagger_auto_schema(methods=['post'], request_body=AddTokenSerilizer)
    @action(detail=False, methods=['post'])
    def post(self, request, *args, **kwargs):
        """
        This method adds Github token into system
        input   -- name
        input   -- token        
        """
        serializer = AddTokenSerilizer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            GithubToken.objects.create(name=data['name'], token=data['token'])
            return Response({"message": "OK"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)
