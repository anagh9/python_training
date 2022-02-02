# DRF VIEW 
# Function Based API VIEW IN DGF

"""
This wrapper provide a few bits of functionality such as making sire uou recireve Request instances in your view, and adding context to Response objects so that content negotition can be performed.

The wrapper also provide behaviour such as returning 405 method not allowed responses when appropriate, and handling any ParseError exceptions that occur when accessing request.data ith malformed input.

By default only GET methods will be accepted . Other methods will respond with "405 Method Not allowed".

syntax :-
@api_view() #default get

@api_view(['GET','POST','PUT','DELETE'])
def function_name(request):
    --
    --

ex :-
# In views.py

from rest_framework.decorators import api_view
from rest_framework.responses import Response
from rest_framework import status

@api_view(['GET'])
def student_list(request):
    if request.method == 'GET':
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)

@api_view(["POST"])
def student_list(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {"msg":"Data Created"}
            
            return Response(res,status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST) 
"""
# PUT- For Updation of comptete data 
# PATCH - For Partial Data Updation

"""
request_query_params - request.query_parmas is a more correctly synonym for request.GET

For clarity inside your code, we recommend using request.query_params instead of the Django's standard request.GET. Doing so will help keep your codebase more correct and obvious - any HTTP method type may include query parameters, not just GET requests.


## Response 
Response objects ate initialized with data ,which should consist of native Python primitives. REST framework then uses standard HTTP content negotiation to determine how it should render the final response content.

Response class simply provides anicer inteface for returning WEb API responses,that can be rendered to multiple formats.

Syntax: -
Response(data,status=None,template_name=None,headers=None,content_type=None)
"""

# CRUD Operation using FunctionViews 
"""
- create models 
- register to admin
- create superuser
- create serializers.py make ModelSerializer
- create Views function
ex:- 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer

@api_view(['GET','POST','PUT','DELETE'])
def student_api(request,pk=None):
    if request.method == 'GET':
        # id = request.data.get(id)
        id = pk
        if id is not None:
            stu = Student.objects.get(id= id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerialzer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid:
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors)

    if request.method == 'PATCH':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid:
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method =='DELETE':
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})


"""
 