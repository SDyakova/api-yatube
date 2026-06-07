from rest_framework import serializers

from posts.models import Comment, Group, Post


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для групп."""

    class Meta:
        model = Group
        fields = ("id", "title", "slug", "description")


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для постов."""

    class Meta:
        model = Post
        fields = ("id", "text", "author", "image", "pub_date", "group")
        read_only_fields = ("author",)


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментариев."""

    class Meta:
        model = Comment
        fields = ("id", "text", "author", "post", "created")
        read_only_fields = ("author", "post")
