from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import F


from main.models import Post, Comment
from main.serializers import CommentSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["action"] = self.action
        return context

    @action(detail=True, methods=["POST"])
    def upvote(self, request, pk):
        get_object_or_404(self.queryset, pk=pk)
        self.queryset.filter(pk=pk).update(upvote=F("upvote") + 1)
        serializer = self.get_serializer(self.queryset.get(pk=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
