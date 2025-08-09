from rest_framework import serializers
from .models import Post

class Postserializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "title",
            "body",
            "created_at"
        )

