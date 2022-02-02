from re import X
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .serializers import Comment, CommentSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

# @api_view(['GET'])
# def check(request):
#     if request.method == 'GET':
#         comment = Comment(email='leila@example.com', content='foo bar')
#         serializer = CommentSerializer(comment)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type='application/json')
