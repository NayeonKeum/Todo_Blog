from rest_framework import serializers
from todoapp.models import Post
from todoapp.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post_id", "contents","created_at","updated_at")

    def to_representation(self, instance):
        self.fields['post_id'] =  PostRepresentationSerializer(read_only=True)
        return super(CommentSerializer, self).to_representation(instance)


class PostSerializer(serializers.ModelSerializer):
    post = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ("id", "title", "contents", "created_at","updated_at", "post")

class PostRepresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "contents","created_at","updated_at")
