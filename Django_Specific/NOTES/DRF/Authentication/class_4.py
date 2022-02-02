# Function Based Views Permission 

from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET','POST','PUT','PATCH','DELETE'])
@authentication_classes([BaseAuthentication])
@permission_classes([IsAuthenticated])
def studentapi(request,pk=None):
    if request.method == 'GET':
        id = pk 
        if id is not None :
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
