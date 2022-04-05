from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Super_TypesSerializer
from .models import Super_Types

@api_view(['GET'])
def super_types_list(request):
    super_type = Super_Types.objects.all()

    serializer = Super_TypesSerializer(super_type, many=True)



    return Response(serializer.data)
