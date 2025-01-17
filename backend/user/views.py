from django.utils.translation import gettext as _
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .serializers import UserSerializer

# Create your views here.
class User(APIView):
    def post(self, request):
        # Check that we are not trying to create super user or staff user
        errors = {}
        if 'is_superuser' in request.data:
            errors['is_superuser'] = _("Unauthorized to create super user.")
        if 'is_staff' in request.data:
            errors['is_staff'] = _("Unauthorized to create staff user.")
        if errors:
            return Response(errors, HTTP_400_BAD_REQUEST)

        # Create user
        serializer: UserSerializer = UserSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)
