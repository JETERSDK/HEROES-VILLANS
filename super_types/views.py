from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Super_TypesSerializer
from .models import Super_Types

@api_view(['GET', 'POST'])
def super_types_list(request):
    if request.method == 'GET':
       super_type = Super_Types.objects.all()
       serializer = Super_TypesSerializer(super_type, many=True)
       return Response(serializer.data)
    elif request.method == 'POST':
         serializer = Super_TypesSerializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
           



        
          
