from datetime import datetime
class Comment:
    def __init__(self, email, content, created=None) -> None:
        self.email = email
        self.content = content 
        self.created = created or datetime.now()

comment = Comment(email="anagh9931@gmail.com",content="lorem ipsum lorem ipsum lorem ipsum lorem ,ipsum")

from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

serializer = CommentSerializer(comment)
# print(serializer.data)