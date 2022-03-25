from rest_framework import serializers

from main.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ("author",)

    def create(self, validated_data):
        request = self.context.get("request")
        author = request.user
        print(author, "asdasdasdasd")
        post = Post.objects.create(author=author, **validated_data)
        return post

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["author"] = instance.author.email
        return representation


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ("author",)

    def create(self, validated_data):
        request = self.context.get("request")
        author = request.user
        comment = Comment.objects.create(author=author, **validated_data)
        return comment

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["author"] = instance.author.email
        return representation
